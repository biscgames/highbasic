# 2025 BISCGAMES
# --- DISCORD: biscgames
# --- GITHUB: biscgames
# PLEASE DO NOT COPY ANY OF MY CODE, THANK YOU
# YOU MAY ONLY FORK THE REPOSITORY FOR MAJOR CODE CHANGES, AND NOTHING MINOR

# var message "Hello, World!"
# println $message

from shlex import split as lexSplit
from sys import argv as args

variables = {
    "!ver": "1_0"
}
functions = {}

def interpretEach(code:list):
    for token in code:
        token = token.strip()
        if not token:
            continue
        tokenSplit = lexSplit(token," ")
        functions[tokenSplit[0]](tokenSplit[1:])

def convertToNum(value:str):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except:
            return value
def isReferencingVar(value:str):
    return value.startswith("$")
def quote(value):
    try: return float(value)
    except: return "\"{}\"".format(value)
def testForVariable(value:str):
    # $ IS THE SYMBOL FOR VARIABLE REFERENCE
    if isReferencingVar(value): return variables[value[1:]]
    else: return value
def println(arg:list):
    print(testForVariable(arg[0]))
def var(arg:list):
    if not arg[0].startswith("!"):
        variables[arg[0]] = convertToNum(testForVariable(arg[1])) if str(testForVariable(arg[1])).isdigit() else testForVariable(arg[1])
    else: 
        print("Attempt to modify read-only variable handled with this message. Variable: {}".format(arg[0]))
def operator(arg:list):
    left = arg[0]
    if isinstance(variables[left],str):
        rights = arg[1:-1]
    else:
        rights = [convertToNum(testForVariable(s)) for s in arg[1:-1]]
    op = arg[-1]

    for right in rights:
        rightVal = testForVariable(str(right))
        if isinstance(variables[left],str):
            if op == "+":
                variables[left] += str(rightVal)
            elif op == "*":
                variables[left] = variables[left] * convertToNum(rightVal)
        else:
            if op == "+":
                variables[left] += convertToNum(rightVal)
            elif op == "-":
                variables[left] -= convertToNum(rightVal)
            elif op == "*":
                variables[left] *= convertToNum(rightVal)
            elif op == "/":
                variables[left] /= convertToNum(rightVal)
macros = {
    "exampleMacro": ["println \"Hello, World!\""]
}
def passfunc(arg:list):
    pass
def macro(arg:list):
    if not arg[0] in macros:
        macros[arg[0]] = []
    else:
        interpretEach(macros[arg[0]])
def inItem(arg:list):
    if arg[0] == "macro":
        macros[arg[1]].append(" ".join(arg[2:]))
def readln(arg:list):
    if not arg[1].startswith("!"): variables[arg[1]] = input(arg[0])
    else: print("Attempt to modify read-only variable handled with this message. Variable: {}".format(arg[1]))
def ifhb(arg:list):
    true = " ".join(arg[2:])
    if int(variables[arg[0]]) == int(testForVariable(arg[1])):
        interpretEach([true])
def unless(arg:list):
    true = " ".join(arg[2:])
    if int(variables[arg[0]]) != int(testForVariable(arg[1])):
        interpretEach([true])
def ifStr(arg:list):
    true = " ".join(arg[2:])
    if str(variables[arg[0]]) == str(testForVariable(arg[1])):
        interpretEach([true])
def unlessStr(arg:list):
    true = " ".join(arg[2:])
    if str(variables[arg[0]]) != str(testForVariable(arg[1])):
        interpretEach([true])
functions = {
    "var":var,
    "operator":operator,
    "println":println,
    ":":passfunc,
    "#":passfunc,
    "macro":macro,
    "in":inItem,
    "readln":readln,
    "equalInt": ifhb,
    "unlessInt": unless,
    "equalString": ifStr,
    "unlessString": unlessStr,
}

def main():
    if len(args) < 2:
        code = input("Welcome to HighBasic\n!ver: {}\nAdd an argument for filename next time to interpret a .hb file!\n>> ".format(variables["!ver"])).split("\n")
    else:
        try:
            with open(args[1],"r") as f:
                code = f.readlines()
        except:
            print("Filepath \"{}\" is not valid.".format(args[1]))
            exit(1)
    interpretEach(code)


if __name__ == "__main__":
    main()