import re
regex =  r"^[a-zA-Z0-9]+ [a-zA-Z0-9_-]$"
reegex = r"^[A-Z][A-Za-z0-9 _-]+(<[a-zA-Z0-9_].+>)?$"
name = input()
if re.match(regex, name):
    print("t")
else:
    print("f")
