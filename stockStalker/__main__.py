import argparse
from functions import printer, app

VERSION = "0.0.1"


def main():
    parser = argparse.ArgumentParser(
        description="Stock Portfolio Tracking CLI"
    )

    # adding arguments
    parser.add_argument(
            "-s",
            "--show",
            default=False,
            help="show portfolio with details",
            action="store_true"
        )
    parser.add_argument(
            "-a",
            "--add",
            default=False,
            help="add entry to portfolio",
            action="store_true"
        )
    args = parser.parse_args()
    printer.print_covid19_cli_info(VERSION)
    app.run(args)
    printer.print_covid19_cli_credits()


if __name__=="__main__":
    main()
