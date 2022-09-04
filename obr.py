import re

while True:
    try:  
        s = input()
        match = re.search(r"<td>(\d+\.\d+\.\d+\.\d+)+</td>",s)
        if match:
            print(match.group(1),end=':')
        match = re.search(r"<td>(\d+)+</td>",s)
        if match:
            print(match.group(1),end='\n')
    except:
        break

print()