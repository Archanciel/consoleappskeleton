import unittest
import os,sys,inspect
from io import StringIO

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from requester import Requester
from commandcrypto import CommandCrypto
from commandquit import CommandQuit
from commanderror import CommandError


class TestRequester(unittest.TestCase):
    '''
    -teste input crypto + fiat avec ou sans
    nosave ou ns
    
    -teste input crypto avec 0 price/oate,
    1 price/date, n price/date
    
    -idem 0, 1, n fiats
    
    -varie order crypto list/fiat list/
    nosave command
    '''
    def setUp(self):
        requester = Requester()
        requester.commandCrypto = CommandCrypto(None)
        requester.commandQuit = CommandQuit(sys)
        self.commandError = CommandError(None)
        requester.commandError = self.commandError
        self.requester = requester


    def test_getUserCommand(self):
        inputStr = "oo btc [5/7 0.0015899 6/7 0.00153] [usd-chf] -nosave"
        userCommand = self.requester._getUserCommand(inputStr, inputStr.upper())
        self.assertEqual(userCommand, 'OO')


    def testRequestUserCommandNoCommand(self):
        stdin = sys.stdin
        sys.stdin = StringIO("btc [5/7 0.0015899 6/7 0.00153] -nosave")
        cryptoCommand = self.requester.request()

        self.assertIsInstance(cryptoCommand, CommandError)

        sys.stdin = stdin


if __name__ == '__main__':
    unittest.main()