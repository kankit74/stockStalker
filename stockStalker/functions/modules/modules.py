import json
import os
from datetime import datetime
from functions import printer, logger

rangebi = printer.Rangebi()

DATA_FILE = '/home/anksh/stockStalker/data/portfolio_one.json'


def display_portfolio():
    data = json_read(DATA_FILE)
    for share_details in data['current_portfolio']:
        print(share_details)


def buy_transaction():
    date_today = datetime.now().strftime("%d/%m/%Y")
    while True:
        print(
            "| Add a Buy Transaction:"
        )
        """ b/s type of transaction
        print(
            "  ",
            rangebi.get_in_warning(
                "Type of Transaction (b/s): "
            ),
            end=""
        )
        type_of_transaction = input()
        if not type_of_transaction or type_of_transaction not in ['b', 'B', 'S', 's']:
            raise Exception("EMPTY_FIELD")
        """
        # input
        print(
            "  ",
            rangebi.get_in_warning(
                "Date of Transaction (default=Today): "
            ),
            end=""
        )
        try:
            date_of_transaction = input()
            date_of_transaction = datetime.stptime(date_of_transaction, "%d/%m/%Y")
        except:
            date_of_transaction = date_today
        # input
        print(
            "  ",
            rangebi.get_in_warning(
                "Name of Share: "
            ),
            end=""
        )
        name_of_share = input()
        if not name_of_share:
            raise Exception("EMPTY_FIELD")
        # input
        print(
            "  ",
            rangebi.get_in_warning(
                "Price of Share: "
            ),
            end=""
        )
        price_of_share = float(input())
        # input
        print(
            "  ",
            rangebi.get_in_warning(
                "Quantity: "
            ),
            end=""
        )
        quantinty = int(input())
        # output
        print(
            "  ",
            rangebi.get_in_warning(
                "Total Costs:"
            ),
            "Rs.",
            price_of_share * quantinty
        )
        printer.new_lines()
        print(
            "| ",
            "Do you want to continue? (y/n):",
            end=""
        )

        c = input()
        if c in ['y', 'Y', 'Yes', 'YES', 'yes']:
            return [
                date_of_transaction,
                name_of_share,
                price_of_share,
                quantinty,
                price_of_share * quantinty
            ]
        else:
            printer.new_lines(2)


def sell_transaction():
    # print available shares
    # select from above share
    # enter quantity and price to sell on that
    # finally recordd teransactino
    return []


def record_transaction(type_of_transaction, share_details):
    data = json_read(DATA_FILE)
    if (type_of_transaction == 'b'):
        lat_id = int(data['lat_id']) + 1
        share = {}
        data['lat_id'] = lat_id
        share['share_id'] = lat_id
        share['date_of_transaction'] = share_details[0]
        share['name_of_share'] = share_details[1]
        share['price_of_share'] = share_details[2]
        share['quantity'] = share_details[3]
        share['total_cost'] = share_details[4]
        data['current_portfolio'].append(share)
        data['buy_transactions'].append(share)
    elif (type_of_transaction == 's'):
        pass
    json_write(DATA_FILE, data)


def json_read(file_name):
   with open(file_name) as f:
       return(json.load(f))


def json_write(file_name, data):
   with open(file_name, "w") as f:
       f.write(json.dumps(data))
