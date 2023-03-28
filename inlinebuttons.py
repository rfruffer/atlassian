from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup

import jira

Approve = "Approve"
Edit = "Edit"
Create = "Create"
Project1 = "Project1"
Project2 = "Project2"
Project3 = "Project3"
Project4 = "Project4"
Project5 = "Project5"
Project6 = "Project6"
selProject1 = "selProject1"
selProject2 = "selProject2"
selProject3 = "selProject3"
selProject4 = "selProject4"
selProject5 = "selProject5"
selProject6 = "selProject6"

TITLES = {
    Approve : "Потдвердить",
    Edit : "Изменить",
    Create : "Создать",
    Project1 : "☑️%s" %(jira.SUP),
    Project2 : "☑️%s" %(jira.SD),
    Project3 : "☑️%s" %(jira.NOTIFY),
    Project4 : "☑️%s" %(jira.INFRA),
    Project5 : "☑️%s" %(jira.QAT),
    Project6 : "☑️%s" %(jira.RKK),
    selProject1 : "✅%s" %(jira.SUP),
    selProject2 : "✅%s" %(jira.SD),
    selProject3 : "️✅%s" %(jira.NOTIFY),
    selProject4 : "✅️%s" %(jira.INFRA),
    selProject5 : "✅️%s" %(jira.QAT),
    selProject6 : "✅️%s" %(jira.RKK),
}

inline_projects = [
    Project1,
    Project2,
    Project3,
    Project4,
    Project5,
    Project6
]
inline_projects1 = [
    selProject1,
    Project2,
    Project3,
    Project4,
    Project5,
    Project6,
    Approve
]
inline_projects2 = [
    Project1,
    selProject2,
    Project3,
    Project4,
    Project5,
    Project6,
    Approve
]
inline_projects3 = [
    Project1,
    Project2,
    selProject3,
    Project4,
    Project5,
    Project6,
    Approve
]
inline_projects4 = [
    Project1,
    Project2,
    Project3,
    selProject4,
    Project5,
    Project6,
    Approve
]
inline_projects5 = [
    Project1,
    Project2,
    Project3,
    Project4,
    selProject5,
    Project6,
    Approve
]
inline_projects6 = [
    Project1,
    Project2,
    Project3,
    Project4,
    Project5,
    selProject6,
    Approve
]

inline_main = [
    Approve
]

inline_edit = [
    Approve,
    Edit
]

inline_create = [
    Create
]

def get_inline_keyboard(resultArray):
    keyboard = []
    arrayElements = []
    for element in resultArray:
        result = InlineKeyboardButton(TITLES[element], callback_data=element)
        arrayElements.append(result)
    if len(arrayElements) == 1:
        keyboard.append([arrayElements[0]])
    else:
        while len(arrayElements)>0:
            if len(arrayElements)>1:
                cut = arrayElements[:2]
                keyboard.append(cut)
                arrayElements.remove(cut[0])
                arrayElements.remove(cut[1])
            if len(arrayElements) == 1:
                keyboard.append([arrayElements[0]])
                break
    return InlineKeyboardMarkup(keyboard)
