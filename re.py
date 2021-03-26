# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import re

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# )
#Q1:[Aa]ndroid
#Q2:没有解决逗号问题

#进阶

res1 = re.match('[.*?[0-9]{3}.*?', s1)
print(res1)

res2 = re.match('([a-z|A-Z]+).*?@([a-z|A-Z]+).*?', s2)
print(res2.group(1))
print(res2.group(2))
s="<a href='https://regexone.com'>Link</a>"
res3 = re.match('<([a-z|A-Z]+).*?',s3)
print(res3.group(1))
res4 = re.match('(\w+).(jpg|png|gif)(?!\.)', s4)
print(res4.group(1))
print(res4.group(2))
s5="https://s3cur3-server.com:9999/"
res5 = re.match('([a-z|A-Z]+)://(.*?):?(\d+)*/.*?',s5)
print(res5.group(1))
print(res5.group(2))
print(res5.group(3))
s6 = "E/( 1553): at widget.List.fillFrom(ListView.java:709)"
res6 = re.match('E/( 1553):/\s+/at widget.List.(\w+)/((.*?):(\d+)/)',s6)
print(res6.group(1))

