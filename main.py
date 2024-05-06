FEATURE_NEW_EXTENSIONS_PAGE = "FeatureNewExtensions"
ADVANCED_OPTIONS_PAGE = "AdvancedOptionsPage"
FEATURES_INSTALLATION_PAGE = "FeaturesInstallationPage"
SCHEDULING_MANAGEMENT_SYSTEM_MAIN_PAGE = "SchedulingManagementSystemMainPage"
DAILY_SCHEDULE_PAGE = "DailySchedulePage"
TUTORIAL_PAGE = "TutorialPage"
EMAIL_SUPPORT_PAGE = "EmailSupportPage"
ADD_TASK_PAGE = "AddTaskPage"
MODIFY_TASK_PAGE = "ModifyTaskPage"


class Task:
    """
    Represents a task in the scheduling management system.

    Attributes:
        content (str): The description of the task.
        index (int): The index position of the task within a day.
        belong_week (str): The day of the week the task belongs to.
        priority (str): The priority of the task, default is 'non-urgent'.
    """

    def __init__(self, content, index, belong_week, priority='non-urgent'):
        """
        Initializes the Task with content, index, belonging week, and priority.
        """
        self._content = content
        self._index = index
        self._belong_week = belong_week
        self._priority = priority

    def getContent(self):
        """
        Returns the content of the task.
        """
        return self._content

    def getIndex(self):
        """
        Returns the index of the task.
        """
        return self._index

    def getPriority(self):
        """
        Returns the priority of the task.
        """
        return self._priority

    def getBelongWeek(self):
        """
        Returns the week day the task belongs to.
        """
        return self._belong_week

    def setContent(self, content):
        """
        Sets the content of the task.
        """
        self._content = content

    def setPriority(self, priority):
        """
        Sets the priority of the task.
        """
        self._priority = priority


def DisplayFeatureNewExtensions():
    """
    Displays new features available in the system.
    """
    print("\n\n\n")
    print("Feature New Extensions:\n- Calculate Completions at runtime \n- "
          "Mark tasks to urgent or non-urgent")
    print("\n")


def DisplayAdvancedOptions():
    """
    Displays advanced options for managing tasks.
    """
    print("Advanced Options:")
    print("- It takes extra time to deal with new mark tasks to\nurgent "
          "or non-urgent functions.")
    print("\n")


def DisplayFeaturesInstallation():
    """
    Displays options for features installation.
    """
    print("Features Installation: ")
    print("- A. Typical")
    print("- B. Custom")
    print("\n")


def DisplaySchedulingManagementSystemMain():
    """
    Displays the main page of the Scheduling Management System.
    """
    print("Scheduling Management System: ")
    print("\n")


def DisplayEmailSupport():
    """
    Displays the email support contact information.
    """
    print("Support: For further assistance, please contact liuj8@oregonstate.edu.")
    print("\n")


def DisplayTutorial():
    """
    Displays a comprehensive tutorial for using the Scheduling Management System.
    """
    print("Tutorial for Schedule Management System\n")
    print("Welcome to the Schedule Management System! This system helps you manage your weekly tasks \n"
          "efficiently, allowing you to add, prioritize, and review tasks for each day of the week. \n"
          "Below, you'll find a guide on how to use the different features of our system.\n")

    print("Getting Started\n")
    print("1. Open the System: When you first open the system, you'll be greeted by the Feature New \n"
          "Extensions page. This page introduces new features that can help you manage your tasks better.\n")
    print("2. Navigate the System: You can navigate through the system using simple text commands. \n"
          "Just type the command and press Enter.\n")

    print("Main Commands\n")
    print("Type 'Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday': To view and manage tasks for \n"
          "a specific day.\n")
    print("Type 'mail', 'Mail' or 'M': To access email support for any inquiries or issues.\n")
    print("Type 'tutorial', 'Tutorial' or 'T': To view this tutorial page anytime you need help.\n")
    print("Type 'Q' or 'quit': To exit the system.\n")

    print("Viewing and Managing Daily Tasks\n")
    print("Select a Day: To check tasks for a specific day, type the day (e.g., 'Monday'). This will display \n"
          "all the tasks scheduled for that day along with their priorities.\n")
    print("Add a Task: If you want to add a new task, type 'add' when you are viewing the daily tasks. \n"
          "You'll be prompted to enter the task details.\n")
    print("Modify Tasks: If you want to change a task's priority or details, simply type the number of the task \n"
          "listed on the day's schedule, and follow the prompts to make adjustments.\n")

    print("Additional Features\n")
    print("Feature Installation: At any time, you can choose to install additional features for managing tasks \n"
          "by navigating to the Feature Installation page. Choose 'Typical' for standard installations or \n"
          "'Custom' for more personalized options.\n")
    print("Advanced Options: For advanced management of tasks, navigate to the Advanced Options page from the \n"
          "Feature New Extensions page by pressing the Enter key.\n")

    print("Email Support\n")
    print("If you encounter any issues or have questions, you can reach out to our support team by typing 'mail'. \n"
          "You'll be directed to the Email Support page where you can get more detailed help.\n")

    print("Exiting the System\n")
    print("To exit the system, simply type 'Q' or 'quit'. This will safely close the application.\n")
    print("\n")


def DisplayDailySchedule(date, customFeatureChoice):
    """
    Displays the tasks scheduled for a specific day.

    Args:
        date (str): The day of the week to display tasks for.
    """
    weekList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for weekIndex in range(0, 7):
        if date == weekList[weekIndex]:
            print(weekList[weekIndex] + ': ')
            taskAmount = len(weekTaskList[weekIndex])
            for taskIndex in range(0, taskAmount):
                if customFeatureChoice == 'A':
                    print(str(taskIndex + 1) + ". " + weekTaskList[weekIndex][taskIndex].getContent()
                          + " Priority: " + weekTaskList[weekIndex][taskIndex].getPriority())
                elif customFeatureChoice == 'B':
                    print(str(taskIndex + 1) + ". " + weekTaskList[weekIndex][taskIndex].getContent())
    print("\n")
    return date


def DisplayAddTask(currentDate):
    """
    Prompts user to add a task for a specific date.

    Args:
        currentDate (str): The date for which the task is being added.
    """
    print("Add task for " + currentDate + ": ")

def DisplayTaskModify(date, index):
    """
    Display task modify page.
    """
    weekList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for weekIndex in range(0, 7):
        if date == weekList[weekIndex]:
            currentTask = weekTaskList[weekIndex][index - 1]
            print('Current task: ' + str(index) + '. ' + currentTask.getContent())
            print("\n")
            return currentTask


def DisplayCommands(status):
    """
    Displays available commands based on the current page status.

    Args:
        status (str): The identifier of the current page.
    """
    if status == FEATURE_NEW_EXTENSIONS_PAGE or status == ADVANCED_OPTIONS_PAGE:
        print("COMMANDS:")
        print("- Type the Enter key to go ahead.")
        print("- Type 'Q' or 'quit' to leave.")
        print("\n")
    elif status == FEATURES_INSTALLATION_PAGE:
        print("COMMANDS:")
        print("- Type 'A' for typical feature's installation, while\n type 'B' for custom feature's installation.")
        print("- Type 'Q' or 'quit' to leave.")
        print("\n")
    elif status == SCHEDULING_MANAGEMENT_SYSTEM_MAIN_PAGE:
        print("COMMANDS:")
        print("- Type 'Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday' to check and manage "
              "daily tasks from Monday to Sunday.")
        print("- Type 'mail', 'Mail' or 'M' to access email support for any inquiries or issues.")
        print("- Type 'tutorial', 'Tutorial' or 'T' to access help tutorials and guides.")
        print("- Type 'Q' or 'quit' to leave.")
        print("\n")
    elif status == DAILY_SCHEDULE_PAGE:
        print("COMMANDS:")
        print("- Type 'Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday' to check and manage "
              "daily tasks from Monday to Sunday.")
        print("- Type integer like 1/2/7/etc to modify certain tasks.")
        print("- Type 'add', 'Add' or 'A' to add tasks.")
        print("- Type 'mail', 'Mail' or 'M' to access email support for any inquiries or issues.")
        print("- Type 'tutorial', 'Tutorial' or 'T' to access help tutorials and guides.")
        print("- Type 'Q' or 'quit' to leave.")
        print("\n")
    elif status == ADD_TASK_PAGE:
        print("COMMANDS:")
        print("- Type  your tasks which cannot be noun or greater than 40 words.")
        print("\n")
    elif status == MODIFY_TASK_PAGE:
        print("COMMANDS:")
        print("- Type 'edit', 'Edit' or 'E' to edit tasks.")
        print("- Type 'back', 'Back' or 'B' to return to the previous page.")
        print("- Type 'delete', 'Delete' or 'D' to delete task.")
        print("- Type 'Q' or 'quit' to leave.")
        print("\n")
    elif status == TUTORIAL_PAGE:
        print("COMMANDS:")
        print("- Type 'back', 'Back' or 'B' to return to the main page.")
        print("- Type 'Q' or 'quit' to leave.")
        print("\n")
    elif status == EMAIL_SUPPORT_PAGE:
        print("COMMANDS:")
        print("- Type 'back', 'Back' or 'B' to return to the main page.")
        print("- Type 'Q' or 'quit' to leave.")
        print("\n")


def FeatureNewExtensionsInputEvent():
    """
    Handles user input for the Feature New Extensions page.
    """
    userInput = None

    while True:
        userInput = input("[Enter/Q]: ")
        print("\n")
        if userInput == '':
            # page 2
            DisplayAdvancedOptions()
            DisplayCommands(ADVANCED_OPTIONS_PAGE)
            AdvancedOptionsInputEvent()
            break
        elif userInput == 'Q' or userInput == 'quit':
            break
        else:
            print("Invalid input, try again.")

    return userInput


def AdvancedOptionsInputEvent():
    """
    Handles user input for the Advanced Options page.
    """
    userInput = None

    while True:
        userInput = input("[Enter/Q]: ")
        print("\n")
        if userInput == '':
            # page 2
            DisplayFeaturesInstallation()
            DisplayCommands(FEATURES_INSTALLATION_PAGE)
            FeaturesInstallationInputEvent()
            break
        elif userInput == 'Q' or userInput == 'quit':
            break
        else:
            print("Invalid input, try again.")

    return userInput


def FeaturesInstallationInputEvent():
    """
    Handles user input for the Features Installation page.
    """
    userInput = None

    while True:
        userInput = input("[A/B/Q]: ")
        print("\n")
        if userInput == 'A' or userInput == 'B':
            customFeatureChoice = userInput
            DisplaySchedulingManagementSystemMain()
            DisplayCommands(SCHEDULING_MANAGEMENT_SYSTEM_MAIN_PAGE)
            currentDate = SchedulingManagementSystemMainInputEvent(customFeatureChoice)
            break
        elif userInput == 'Q' or userInput == 'quit':
            break
        else:
            print("Invalid input, try again.")

    return userInput


def MailAndTutorialInputEvent(customFeatureChoice):
    """
    Handles user input for the Mail and Tutorial pages.
    """

    while True:
        userInput = input("[back/quit]: ")
        print("\n")
        if userInput in ['back', 'Back', 'B']:
            DisplaySchedulingManagementSystemMain()
            DisplayCommands(SCHEDULING_MANAGEMENT_SYSTEM_MAIN_PAGE)
            currentDate = SchedulingManagementSystemMainInputEvent(customFeatureChoice)
            break
        elif userInput == 'Q' or userInput == 'quit':
            break
        else:
            print("Invalid input, try again.")

    return userInput


def DailyAddTaskInputEvent(currentDate, customFeatureChoice):
    """
    Handles adding a new task for a specified date.
    """
    userInput = input("Type your task: ")
    weekList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for weekIndex in range(0, 7):
        if currentDate == weekList[weekIndex]:
            newTask = Task(userInput, weekIndex + 1, currentDate)
            weekTaskList[weekIndex].append(newTask)
            if customFeatureChoice == 'A':
                DailyChangePriorityInputEvent(newTask, customFeatureChoice)
                break
            elif customFeatureChoice == 'B':
                DisplayDailySchedule(currentDate, customFeatureChoice)
                DisplayCommands(DAILY_SCHEDULE_PAGE)
                DailyScheduleInputEvent(currentDate, customFeatureChoice)


def DailyChangePriorityInputEvent(currentTask, customFeatureChoice):
    """
    Handles changing the priority of a specific task.
    """
    while True:
        userInput = input("Type the Priority for this task [urgent/non-urgent]: ")
        print("\n")
        if userInput in ['urgent', 'non-urgent']:
            currentTask.setPriority(userInput)
            DisplayDailySchedule(currentTask.getBelongWeek(), customFeatureChoice)
            DisplayCommands(DAILY_SCHEDULE_PAGE)
            DailyScheduleInputEvent(currentTask.getBelongWeek(), customFeatureChoice)
        else:
            print("Invalid input, try again.")

def TaskModifyInputEvent(currentTask, customFeatureChoice):
    """
    Handles modifying a specific task.
    """
    while True:
        userInput = input("[edit/back/delete/Q]: ")

        print("\n")
        if userInput in ['edit', 'Edit', 'E']:
            userInput = input("Type the modified content you cant to change into: \n")
            currentTask.setContent(userInput)
            print("\n")
            DisplayDailySchedule(currentTask.getBelongWeek(), customFeatureChoice)
            DisplayCommands(DAILY_SCHEDULE_PAGE)
            DailyScheduleInputEvent(currentTask.getBelongWeek(), customFeatureChoice)
        else:
            print("Invalid input, try again.")

        # elif userInput in ['back', 'Back', 'B']:
        #     break
        # elif userInput in ['delete', 'Delete', 'D']:
        #     break
        # elif userInput == 'Q' or userInput == 'quit':
        #     break

def ExceedTaskMaximun(currentDate):
    """
    Handles user input for daily task management and navigation.
    """
    weekList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for weekIndex in range(0, 7):
        if currentDate == weekList[weekIndex]:
            totalTaskAmount = len(weekTaskList[weekIndex])
            if totalTaskAmount < 10:
                return False
            else:
                return True


def DailyScheduleInputEvent(currentDate, customFeatureChoice):
    """
    Handles main input events for the scheduling management system.
    """
    while True:
        userInput = input("[Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/1/2/.../add/Sunday/mail/tutorial/Q]: ")

        print("\n")
        if userInput in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                         'Saturday', 'Sunday']:
            DisplayDailySchedule(userInput, customFeatureChoice)
            DisplayCommands(DAILY_SCHEDULE_PAGE)
            DailyScheduleInputEvent(userInput, customFeatureChoice)
            break

        elif userInput.isnumeric():
            currentTask = DisplayTaskModify(currentDate, int(userInput))
            DisplayCommands(MODIFY_TASK_PAGE)
            TaskModifyInputEvent(currentTask, customFeatureChoice)
            break

        elif userInput in ['add', 'Add' or 'A']:
            if ExceedTaskMaximun(currentDate):
                while True:
                    userInput = input("Warning\nOver 10 tasks, this is overwhelming, "
                                      "still want adding more tasks? [Y/N]: ")
                    if userInput == 'Y':
                        DisplayAddTask(currentDate)
                        DisplayCommands(ADD_TASK_PAGE)
                        DailyAddTaskInputEvent(currentDate, customFeatureChoice)
                        break
                    elif userInput == 'N':
                        print("\n")
                        DisplayCommands(DAILY_SCHEDULE_PAGE)
                        DailyScheduleInputEvent(currentDate, customFeatureChoice)
                        break
                    else:
                        print("Invalid input, try again.")
            else:
                DisplayAddTask(currentDate)
                DisplayCommands(ADD_TASK_PAGE)
                DailyAddTaskInputEvent(currentDate, customFeatureChoice)
                break

        elif userInput in ['mail', 'Mail', 'M']:
            DisplayEmailSupport()
            DisplayCommands(EMAIL_SUPPORT_PAGE)
            MailAndTutorialInputEvent(customFeatureChoice)
            break
        elif userInput in ['tutorial', 'Tutorial', 'T']:
            DisplayTutorial()
            DisplayCommands(TUTORIAL_PAGE)
            MailAndTutorialInputEvent(customFeatureChoice)
            break
        elif userInput == 'Q' or userInput == 'quit':
            break
        else:
            print("Invalid input, try again.")


def SchedulingManagementSystemMainInputEvent(customFeatureChoice):
    """
    Handles main input events for the scheduling management system.
    """
    while True:
        userInput = input("[Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday/mail/tutorial/Q]: ")
        print("\n")
        if userInput in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                         'Saturday', 'Sunday']:
            if customFeatureChoice == 'A':
                DisplayDailySchedule(userInput, 'A')
                DisplayCommands(DAILY_SCHEDULE_PAGE)
                DailyScheduleInputEvent(userInput, 'A')
            elif customFeatureChoice == 'B':
                DisplayDailySchedule(userInput, 'B')
                DisplayCommands(DAILY_SCHEDULE_PAGE)
                DailyScheduleInputEvent(userInput, 'B')
        elif userInput in ['mail', 'Mail', 'M']:
            DisplayEmailSupport()
            DisplayCommands(EMAIL_SUPPORT_PAGE)
            MailAndTutorialInputEvent(customFeatureChoice)
            break
        elif userInput in ['tutorial', 'Tutorial', 'T']:
            DisplayTutorial()
            DisplayCommands(TUTORIAL_PAGE)
            MailAndTutorialInputEvent(customFeatureChoice)
            break
        elif userInput == 'Q' or userInput == 'quit':
            break
        else:
            print("Invalid input, try again.")


MondayTask = [Task('44', 1, 'Monday', 'urgent'),
              Task('55', 2, 'Monday', 'urgent'),
              Task('66', 3, 'Monday', 'non-urgent'),
              Task('44', 1, 'Monday', 'urgent'),
              Task('55', 2, 'Monday', 'urgent'),
              Task('66', 3, 'Monday', 'non-urgent'),
              Task('44', 1, 'Monday', 'urgent'),
              Task('55', 2, 'Monday', 'urgent'),
              Task('66', 3, 'Monday', 'non-urgent')
              ]
TuesdayTask = [Task('yiyi', 1, 'Tuesday', 'urgent'),
               Task('ss', 2, 'Tuesday', 'non-urgent'),
               Task('000', 3, 'Tuesday', 'urgent')]
WednesdayTask = []
ThursdayTask = []
FridayTask = []
SaturdayTask = []
SundayTask = []

weekTaskList = [MondayTask, TuesdayTask, WednesdayTask, ThursdayTask,
                FridayTask, SaturdayTask, SundayTask]

while True:
    DisplayFeatureNewExtensions()
    DisplayCommands(FEATURE_NEW_EXTENSIONS_PAGE)
    FeatureNewExtensionsInputEvent()
