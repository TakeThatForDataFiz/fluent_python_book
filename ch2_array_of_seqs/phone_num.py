
def where_is_phone(phone):
    match tuple(str(phone)):
        case ['1', *rest]:
            print("North America/Carribean")
        case ['2', *rest]:
            print("Africa, some territories")
        case ['3' | '4', *rest]:
            print("Europe")
        case _:
            print("Unknown")

if __name__ == '__main__':
    where_is_phone('66')