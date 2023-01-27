from synochat.webhooks import IncomingWebhook
Send = False
def Message(server, Message):
    if (server == "General"):
        token = "NjuAQmiT5AjGjUnipFTahF73yt9giD5QUTd3N4wR06PdDK7s2kucTXEr7ZpkvkwS"
        print("Sending Messages To: General")
    elif (server == "SFW"):
        token = "X0d0NKXZYtESSITTEH1wE3sAopw1awXKbBwyGU8B1OGevbwZst8WvTegGYBrhf4j"
        print("Sending Messages To: SFW Chat")
    elif (server == "ToDoList"):
        token = "ysAeOOV9eaBtjPmLbQ0XHYhpwGKT3d2gS4HyvZElWl32wDOjYzmmcKaLEJHmttgR"
        print("Sending Messages To: To-Do List")
    elif (server == "Reviewed"):
        token = "rINoCshdjkNkVCiHaqZ10I9KJd94PBfWBwXFCGaGeAnJahH5P0KrqWcK97GT1oPP"
        print("Sending Messages To: Reviewed")
    else:
        WebToken = "NjuAQmiT5AjGjUnipFTahF73yt9giD5QUTd3N4wR06PdDK7s2kucTXEr7ZpkvkwS"
        token = WebToken
        webhook = IncomingWebhook('jcmc-tardis.de3.quickconnect.to', token, port=38399, verify_ssl=False)
        webhook.send('Incorect Command Issued Looking for: '+ server +' Channel')
    webhook = IncomingWebhook('jcmc-tardis.de3.quickconnect.to', token, port=38399, verify_ssl=False)
    if Send:
        webhook.send(Message)