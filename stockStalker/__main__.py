import argparse
from functions import printer, app

VERSION = "0.0.1"


def main():
    parser = argparse.ArgumentParser(
        description="Stock Portfolio Tracking CLI"
    )

    parser.add_argument(
            "-d",
            "--display",
            default=False,
            help="display portfolio",
            action="store_true"
        )
    parser.add_argument(
            "-b",
            "--buy",
            default=False,
            help="add buy entry to portfolio",
            action="store_true"
        )
    parser.add_argument(
        "-s",
        "--sell",
        default=False,
        help="add sell entry to portfolio",
        action="store_true"
    )

    args = parser.parse_args()
    printer.print_covid19_cli_info(VERSION)
    app.run(args)
    printer.print_covid19_cli_credits()


if __name__=="__main__":
    main()
