#!/usr/bin/env python3


shooping_list = {}


def add():
    print("Enter item to add")
    item = input("> ")
    print("Enter amount")
    amount = input("> ")

    shooping_list[item] = amount


def remove():
    print("Enter item to remove")
    item = input("> ")
    shooping_list.pop(item)


def view():
    for item, amount in shooping_list.items():
        print(f"{item}: {amount}")


commands = {"add": add, "remove": remove}


def main():
    while True:
        print("[remove | add]")
        cmd = input("> ").split()[0].strip()
        commands[cmd]()
        view()


if __name__ == "__main__":
    main()
