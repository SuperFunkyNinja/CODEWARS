import re


def validBraces(string):
    pattern = re.compile(r"\(\)|\[\]|\{\}")
    gp = pattern.search(string)
    string = str.replace(string, gp.group(0), "")
    print(len(string))
    print(gp)
    if len(string) == 0:
        print("true")
        return
    if 
    else:
        validBraces(string)
    # else:
    #     return False
    # if len(string) == 0:
    #     return True
    # elif gp is not None:
    #     return False
    # else:
    #     validBraces(string)


print(validBraces("[({})]()[]"))
