import module1
from module2 import modfunc1, modfunc2
from module3.logging import writelog

state = {
    "key1": ["val1", "val2"],
    "key2": 100
}

# function calls

val1 = module1.func1("arg1", "arg2", param1="arg3")

val2 = modfunc1(param1="arg1", param2="arg2", param3=10)

val3 = modfunc2(1, 2, 3, "arg4", "arg5")

if val1 > 0 or val2 > 0 or val3 > 0:
    writelog("error has occured")
    exit()
else:
    writelog("values are valid")