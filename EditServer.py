# Server-side (editServer.py)
import pika
import json
import uuid

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

def edit_task(currentTask, inputString):
    currentTask.setContent(inputString)
    return currentTask

def edit_task_priority(currentTask, inputPriorityString):
    currentTask.setPriority(inputPriorityString)
    return currentTask

def on_request(ch, method, props, body):
    try:
        request = json.loads(body)

        task_data = request.get('task_data', {})
        task = Task(task_data['content'], task_data['index'], task_data['belong_week'], task_data['priority'])

        if request['task'] == 'edit_task':
            new_content = request.get('new_content', '')
            response = edit_task(task, new_content)
        elif request['task'] == 'edit_task_priority':
            new_priority = request.get('new_priority', '')
            response = edit_task_priority(task, new_priority)
        else:
            response = 'Invalid Task'

        response = response.__dict__  # Convert Task object to dictionary for JSON serialization

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

    channel.queue_declare(queue='EditQueue')
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='EditQueue', on_message_callback=on_request)

    print(" [x] Awaiting RPC requests")
    channel.start_consuming()

if __name__ == "__main__":
    start_server()
