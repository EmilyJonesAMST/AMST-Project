from synochat.webhooks import IncomingWebhook
Send = False
def Message(server, Message):
    if (server == "General"):
        token = ""
        print("Sending Messages To: General")
    elif (server == "SFW"):
        token = ""
        print("Sending Messages To: SFW Chat")
    elif (server == "ToDoList"):
        token = ""
        print("Sending Messages To: To-Do List")
    elif (server == "Reviewed"):
        token = ""
        print("Sending Messages To: Reviewed")
    else:
        WebToken = ""
        token = WebToken
        webhook = IncomingWebhook('', token, port=38399, verify_ssl=False)
        webhook.send('Incorect Command Issued Looking for: '+ server +' Channel')
    webhook = IncomingWebhook('', token, port=38399, verify_ssl=False)
    if Send:
        webhook.send(Message)
