#sys1.py
import sys

result=0
for number in sys.argv[1:]:
    result+=int(number)

print(result)