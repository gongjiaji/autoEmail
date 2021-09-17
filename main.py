from exchangelib import Credentials  #  pip install exchangelib
from exchangelib import Account
from exchangelib import Message
from exchangelib import Mailbox
from exchangelib import HTMLBody
from exchangelib import FileAttachment
from tqdm import tqdm

import time

emailAdress = ""
emailPassword = ""



def sendEmail(subject, body, receiver):
    # print("sending to",receiver)
    # TODO use system email, ask people to register
    credentials = Credentials(emailAdress,emailPassword)
    account = Account(
        emailAdress, credentials=credentials, autodiscover=True
    )
    m = Message(
        account=account, subject=subject, body=HTMLBody(body), to_recipients=receiver
    )

    # attchment
    # with open("Webinarのご案内.pdf", "rb") as f:
    #     cont = f.read()
    # attchF = FileAttachment(name="Webinarのご案内.pdf", content=cont)
    # m.attach(attchF)

    m.send()


subject = "subject"
body = """
html content
"""

# read email list from file
emailListFilePath = ""
with open(emailListFilePath, "r", encoding='utf-8') as file:
    allEmail = file.readlines()

receiver = []

for x in allEmail:
    x = x.replace("\n", "")
    receiver.append([x])

for x in tqdm(receiver):
    try:
        sendEmail(subject, body, x)
    except:
        print(x, "failed")
        continue
    time.sleep(4)
