#importing important things
from zang import ZangException, Configuration, ConnectorFactory
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

class sms:

    #this is supposed to be a constructor and will set up important variables
    def __init__(self):
        #these will have to be changed for different accounts
        self.sid = ''
        self.authToken = ''

        self.url = 'http://api.zang.io/v2'
        self.configuration = Configuration(self.sid, self.authToken, url=self.url)
        self.smsMessagesConnector = ConnectorFactory(self.configuration).smsMessagesConnector
        self.callsConnector = ConnectorFactory(self.configuration).callsConnector

        #this will have to be changed for different accounts, it's the number the account will use
        self.no='+18559840772'

    #Send a text message:
    #String number is a the number you want to send a text to
    #String text is the text to send
    def sendText(self, number, text):

        try:
           self.smsMessage = self.smsMessagesConnector.sendSmsMessage(to=number,body=text,from_=self.no)
           print(self.smsMessage)
        except ZangException as ze:
            print(ze)
