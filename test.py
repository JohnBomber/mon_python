import re
t = "i love $"
found = re.findall("\\$", t, re.IGNORECASE)
print(found)
