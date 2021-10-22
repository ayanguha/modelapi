
from O365 import Account

#APP_ID="0a3e158e-7323-4bd8-be9a-6e50b9750e2c"
#SECRET="leB7Q~nAin2yGqtTo9Nu74Ztuvkn2QnjOQY23"


APP_ID="451e13a1-5367-4c83-ba0c-3a1d5583f100"
SECRET="M2N7Q~yIhutMiPIYMFIIfEvvoHaMIr5Frb.Sq"

TENAND_ID="1cabbed0-2d14-43cf-9b61-b2a8803eda0b"
resource="ayan@redclock.onmicrosoft.com"

credentials = (APP_ID, SECRET)

scopes = ['https://graph.microsoft.com/Mail.ReadWrite', 'https://graph.microsoft.com/Mail.Send']

account = Account(credentials, auth_flow_type='credentials', tenant_id=TENAND_ID)
account.authenticate()
print(account.con.token_backend.token)
mailbox = account.mailbox(resource=resource)
inbox = mailbox.inbox_folder()
for message in inbox.get_messages(download_attachments=True):
    if message.has_attachments:
        print(message.attachments)
        for att in message.attachments:
            print(att)
            att.save(location="/Users/ayanguha/project/modelapi/api/handlers")
    print(message)
