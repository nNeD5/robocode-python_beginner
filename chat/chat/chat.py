#!/usr/bin/env python


import os
from bardapi import Bard


token = os.getenv("_BARD_API_KEY")
bard = Bard()
print("Enter you question")
print("Enter exit or q to exit")
while True:
    question = input("> ")
    if question == "exit" or question == "q":
        break

    res = bard.get_answer(question)
    print(res["content"])
print("Bye")
