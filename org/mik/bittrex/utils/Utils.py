import json
from argparse import ArgumentParser
class BitUtils:
    def readKeys(self):
        with open("org/mik/bittrex/app/secrets.json") as secrets_file:
            self.secrets = json.load(secrets_file)
            secrets_file.close()
            return self.secrets
    def buildCommandLineArgument(self):
        parser=ArgumentParser( prog='trade-bittrex', usage="usage: %(prog)s [options] filename", version="%(prog)s 1.0")
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
        parser.add_argument("-m", "--market",
                            action="store",
                            default="BTC-ETH",
                            dest="market",
                            help="Market name  Eg BTC-ETH")
        args = parser.parse_args()
        #print options.currency
        return args

