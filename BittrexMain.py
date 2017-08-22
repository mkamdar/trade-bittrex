from org.mik.bittrex.core.bittrex import Bittrex as bittrex, Bittrex
from org.mik.bittrex.utils.Utils import BitUtils
import optparse

import sys

class BittrexMain:

    def __init__(self):
        self .secrets=BitUtils().readKeys()
        self.bittrex = Bittrex(self.secrets['key'], self.secrets['secret'])

    def main(self):
        self.args=BitUtils().buildCommandLineArgument()
        globals().update(vars(self.args)) #sets all the arguments as global variables. see buildcommandlineArguments and see the dest fileds for variable names
        self.run()
    def run(self):
       if operation == "getbalance":
           balance = self.bittrex.get_balance(currency)
           print (balance)

if __name__ == '__main__':
    BittrexMain().main()
