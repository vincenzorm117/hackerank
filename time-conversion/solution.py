
import re

def timeConversion(s):
    s = s.strip()
    hour, minute, second, pm = re.findall(r"^([0-9]{2}):([0-9]{2}):([0-9]{2})(AM|PM)$", s)[0]
    time = list(map(int, [hour,minute,second]))
    time[0] %= 12
    print(time)
    if pm == 'PM':
        time[0] += 12
    return ':'.join(['%02d' % x for x in time])
    

s = input().strip()
result = timeConversion(s)
print(result)

