from abstractcommand import AbstractCommand

class CommandCrypto(AbstractCommand):
    '''
    Example of a concrete business command
    '''
    def __init__(self, receiver=None, name='', rawParmData='', parsedParmData=''):
        super().__init__(receiver, 'CommandCrypto', rawParmData, parsedParmData)

    def execute(self):
        self.receiver.processCrypto(self.parsedParmData)
