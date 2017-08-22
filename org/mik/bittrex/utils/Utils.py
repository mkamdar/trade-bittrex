import json
from argparse import ArgumentParser
class BitUtils:
    def readKeys(self):
        with open("org/mik/bittrex/app/secrets.json") as secrets_file:
            self.secrets = json.load(secrets_file)
            secrets_file.close()
            return self.secrets
    def buildCommandLineArgument(self):
        parser=ArgumentParser( prog='PROG', usage="usage: %prog [options] filename", version="%prog 1.0")
        parser.add_argument("-o", "--operation",
                          action="store",
                          default="getbalance",
                          dest="operation",
                          help="operation you want to perform. Default is getbalance" )
        parser.add_argument("-c", "--currency",
                          action="store",
                          default="BTC",
                          dest="currency",
                          help="Coin name")

        args = parser.parse_args()
        #print options.currency
        return args

