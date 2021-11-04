import re


def validBraces(string):
    pattern = re.compile(r"\(\)|\[\]|\{\}")
    gp = pattern.search(string)
    if gp is None:
        return "False"
    string = str.replace(string, gp.group(0), "")
    print(string)
    print(gp)
    if len(string) == 0:
        return True
    elif gp is not None:
        return False
    else:
        validBraces(string)


print(validBraces("[({})]()[]"))
