import re


def validBraces(string):
    # if string is None:
    #     print("true")
    #     return True
    if len(string) == 0:
        print("true")
        return True
    pattern = re.compile(r"\(\)|\[\]|\{\}")
    gp = pattern.search(string)
    if gp is None:
        print("false")
        return False
    string = str.replace(string, gp.group(0), "")
    return validBraces(string)


validBraces("[({})]()[[]]{[()}]")
if validBraces("()") is True:
    print("testpassed")
else:
    print("test failed")
validBraces("")
