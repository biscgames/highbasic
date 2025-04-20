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
    "!ver": "1.1_0",
    "!newline": "\n",
    "!emptyline": ""
}
functions = {}

def interpretEach(code:list):
    for i,token in enumerate(code):
        token = token.strip()
        if not token:
            continue
        tokenSplit = lexSplit(token," ")
        try:
            functions[tokenSplit[0]](tokenSplit[1:])
        except Exception as e:
            print("Error in line {}: {}\nException: {}".format(i," ".join(tokenSplit),e))

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
    if isReferencingVar(value):
        while isReferencingVar(value):
            pointer = 0
            while value[pointer] == "$":
                pointer += 1
            val = variables[value[pointer:]]
            value = value.replace(value[pointer:],str(val))
            value = value[1:]
    return value
def println(arg:list):
    print(testForVariable(arg[0]))
def var(arg:list):
    val = testForVariable(arg[0])
    value = convertToNum(testForVariable(arg[1])) if str(testForVariable(arg[1])).isdigit() else testForVariable(arg[1])
    if not val.startswith("!"):
        variables[val] = value
    else: 
        print("Attempt to modify read-only variable handled with this message. Variable: {}".format(arg[0]))
def operator(arg:list):
    left = testForVariable(arg[0])
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
            elif op == "%":
                variables[left] %= convertToNum(rightVal)
macros = {
    "exampleMacro": ["println \"Hello, World!\""]
}
def passfunc(arg:list):
    pass
def macro(arg:list):
    if not testForVariable(arg[0]) in macros:
        macros[testForVariable(arg[0])] = []
    else:
        interpretEach(macros[testForVariable(arg[0])])
def inItem(arg:list):
    if arg[0] == "macro":
        macros[testForVariable(arg[1])].append(" ".join(arg[2:]))
def readln(arg:list):
    if not arg[1].startswith("!"): variables[arg[1]] = input(arg[0])
    else: print("Attempt to modify read-only variable handled with this message. Variable: {}".format(arg[1]))
def ifhb(arg:list):
    true = " ".join(arg[2:])
    if int(variables[testForVariable(arg[0])]) == int(testForVariable(arg[1])):
        interpretEach([true])
def unless(arg:list):
    true = " ".join(arg[2:])
    if int(variables[testForVariable(arg[0])]) != int(testForVariable(arg[1])):
        interpretEach([true])
def ifStr(arg:list):
    true = " ".join(arg[2:])
    if str(variables[testForVariable(arg[0])]) == str(testForVariable(arg[1])):
        interpretEach([true])
def unlessStr(arg:list):
    true = " ".join(arg[2:])
    if str(variables[testForVariable(arg[0])]) != str(testForVariable(arg[1])):
        interpretEach([true])
def string(arg:list):
    val = testForVariable(arg[0])
    if not val.startswith("!"):
        variables[val] = str(testForVariable(arg[1]))
    else: 
        print("Attempt to modify read-only variable handled with this message. Variable: {}".format(arg[0]))
def num(arg:list):
    val = testForVariable(arg[0])
    if not val.startswith("!"):
        variables[val] = convertToNum(testForVariable(arg[1]))
    else: 
        print("Attempt to modify read-only variable handled with this message. Variable: {}".format(arg[0]))
def toNum(arg:list):
    variables[testForVariable(arg[0])] = convertToNum(variables[arg[0]])
def toString(arg:list):
    variables[testForVariable(arg[0])] = str(variables[arg[0]])
def ifDynamic(arg:list):
    pass
def unlessDynamic(arg:list):
    pass
def printtc(arg:list):
    print(testForVariable(arg[0]),end="")
def module(arg:list):
    val = testForVariable(arg[0])
    if len(arg) > 0:
        try:
            with open(val,"r") as f:
                lines = f.readlines()
                if lines[0].strip() == "module":
                    interpretEach(lines[1:])
                else:
                    print("\"Module\" {} is not a valid module. (put \"module\" at the first line of the file to confirm it is a module)".format(arg[0]))
        except Exception as e:
            print("Filepath \"{}\" cannot be run. {}".format(args[1],e))
def destroy(arg:list):
    if arg[0] == "macro":
        if arg[-1] == "r":
            macros[testForVariable(arg[1])] = []
        else:
            del macros[testForVariable(arg[1])]
    if arg[0] == "var":
        del variables[testForVariable(arg[1])]
def concat(arg:list):
    rights = arg[1:]
    for right in rights:
        variables[testForVariable(arg[0])] += testForVariable(right)
functions = {
    "var":var,
    "operator":operator,
    "println":println,
    ":":passfunc,
    "#":passfunc,
    "group": passfunc,
    "macro":macro,
    "in":inItem,
    "readln":readln,
    "equalInt": ifhb,
    "unlessInt": unless,
    "equalString": ifStr,
    "unlessString": unlessStr,
    "if": ifDynamic,
    "unless": unlessDynamic,
    "string": string,
    "num": num,
    "toNum": toNum,
    "toString": toString,
    "print": printtc,
    "module": module,
    "del": destroy,
    "concat": concat
}

def main():
    if len(args) < 2:
        code = input("Welcome to HighBasic\n!ver: {}\nAdd an argument for filename next time to interpret a .hb file!\n>> ".format(variables["!ver"])).split("\n")
    else:
        try:
            with open(args[1],"r") as f:
                lines = f.readlines()
                if lines[0].strip() == "module":
                    code = ["println \"Modules cannot run by theirselves and must be run by a main .hb file.\""]
                else:
                    code = lines
        except Exception as e:
            print("Filepath \"{}\" cannot be run. {}".format(args[1],e))
            exit(1)
    interpretEach(code)


if __name__ == "__main__":
    main()
