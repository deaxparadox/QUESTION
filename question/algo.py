# i = 0

# count = 0
# for _ in range(len(s)):
#     try:
#         index = s.index('a', i)
#         # print("index", index)
#         count += s.count(subs, index)
#     except:
#         break
#     else:
#         i=index + 1
# print(count)

# import re
# for match in re.finditer(subs, s):
#     print(match.start(), match.end())

def count(s, subs):
    marker = 0
    count = 0
    while marker < len(s):
        try:
            # print(s.index(subs,marker))
            marker = s.index(subs, marker) + 1
            count += 1
        except ValueError:
            break
            # print("String not found")
            # marker = len(s)
    return count

s = 'banana'
subs = 'a'
for c in s:
    print(c, count(s, c))