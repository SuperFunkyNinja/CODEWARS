import re


def validBraces(string):
    if string is None:
        print("true")
        return True
    if len(string) == 0:
        print("true")
        return True
    pattern = re.compile(r"\(\)|\[\]|\{\}")
    gp = pattern.search(string)
    if gp is None:
        print("false")
        return False
    string = str.replace(string, gp.group(0), "")
    validBraces(string)


validBraces("[({})]()[[]]{[()}]")
validBraces("()")
validBraces("")
validBraces(None)
