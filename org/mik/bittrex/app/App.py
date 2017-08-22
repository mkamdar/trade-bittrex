from org.mik.bittrex.core.bittrex import Bittrex as bittrex, Bittrex
from org.mik.bittrex.utils.Utils import BitUtils
import optparse

import sys

class App:

    def prepareKeys(self):
        self .secrets=BitUtils().readKeys()
        self.bittrex = Bittrex(self.secrets['key'], self.secrets['secret'])

    def appmain(self):
        #self.prepareKeys()
        self.args=BitUtils().buildCommandLineArgument()
        globals().update(vars(self.args)) #sets all the arguments as global variables. see buildcommandlineArguments and see the dest fileds for variable names
        self.run(currency,operation,market)

    def run(self, curr, op,market):
        self.prepareKeys()
        if op == "getbalance":
            balance = self.bittrex.get_balance(curr)
            print (balance)
        if op == "getbalances":
            balances = self.bittrex.get_balances()
            print (balances)
        if op == "getticker":
            ticker = self.bittrex.get_ticker(market)
            print (ticker)
        if op == "getopenorders":
            ticker = self.bittrex.get_open_orders(market)
            print (ticker)
        if op == "getorderhistory":
            ticker = self.bittrex.get_order_history(market)
            print (ticker)


if __name__ == '__main__':
    BittrexMain().main()
