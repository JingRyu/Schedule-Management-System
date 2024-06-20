# Save this as server.py and run it
import pika
import json

class Task:
    def __init__(self, content, index, belong_week, priority='non-urgent'):
        self._content = content
        self._index = index
        self._belong_week = belong_week
        self._priority = priority

    def getContent(self):
        return self._content

    def getIndex(self):
        return self._index

    def getPriority(self):
        return self._priority

    def getBelongWeek(self):
        return self._belong_week

    def setContent(self, content):
        self._content = content

    def setPriority(self, priority):
        self._priority = priority

def double_check_deletion(userInput):
    if userInput == 'Y':
        return True
    elif userInput == 'N':
        return False
    else:
        return "Invalid input, try again."

def delete_task(currentTask):
    currentTask.setContent('')
    currentTask.setPriority('')
    return currentTask

def on_request(ch, method, props, body):
    try:
        print(f"Received body: {body}")
        request = json.loads(body)
        print(f"Parsed request: {request}")

        if request['task'] == 'DoubleCheckDeletion':
            userInput = request.get('userInput', None)
            response = double_check_deletion(userInput)
        elif request['task'] == 'edit_task':
            task_data = request.get('task_data', {})
            task = Task(task_data['content'], task_data['index'], task_data['belong_week'], task_data['priority'])
            response = delete_task(task)
            response = response.__dict__
        else:
            response = 'Invalid Task'

    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        response = 'Invalid JSON format'
    except Exception as e:
        print(f"Unexpected error: {e}")
        response = 'Error processing request'

    response = json.dumps(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)

def start_server():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='DeletionQueue')
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='DeletionQueue', on_message_callback=on_request)
    print(" [x] Awaiting RPC requests")
    channel.start_consuming()

if __name__ == "__main__":
    start_server()
