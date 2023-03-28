import json

SUP = "(SUP)Support"
SD = "(SD)HelpDesk"
JIRA = "(JIRA)Jira Доработки"
INFRA = "(INFRA)Infrastructure"
QAT = "(QAT)QA team"
RKK = "(RKK)Развитие клиентских каналов"
NOTIFY = "(NOTIFY)Информирование"

mapProject = {
    SUP : "SUP",
    SD : "SD",
    JIRA : "JIRA",
    INFRA : "INFRA",
    QAT : "QAT",
    RKK : "RKK",
    NOTIFY : "NOTIFY"
}

def createIssue (sum, dis, prj, user):
    obj = json.dumps({
        "fields": {
            "summary": sum,
            "customfield_10111": user,
            "issuetype": {
                "id": "10001"
            },
            "project": {
                "key": prj
            },
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "text": dis,
                                "type": "text"
                            }
                        ]
                    }
                ]
            }
        }
    })
    return obj
