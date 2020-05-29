from datetime import datetime

from functions import printer, logger
from functions.modules import modules


rangebi = printer.Rangebi()


def run(args):
    if args.display:
        modules.display_portfolio()
    elif args.buy:
        try:
            share_details = modules.buy_transaction()
            modules.record_transaction('b', share_details)
        except Exception as e:
            print(e)
            logger.log_error("Error Occured Please Try Again")
    elif args.sell:
        try:
            share_deatils = modules.sell_transaction()
            modules.record_transaction('s', share_details)
        except:
            logger.log_error("Error Occured Please Try Again")


if __name__=="__name__":
    print("Forbidden")