#!/usr/bin/python3
# Owned By Yahya

import hidden_4
def principal():
    for i in dir(hidden_4):
        if not (i[0] == '_' and i[1] == '_'):
            print(i)

if __name__ == "__main__":
    principal()
