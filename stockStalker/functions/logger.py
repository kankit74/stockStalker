from functions import printer


def log_error(message):
    rangebi = printer.Rangebi()
    printer.new_lines()
    print(
        rangebi.get_in_danger("| " + message)
    )
