import sys
def merge_the_tools(string, k):
    length = len(string)
    # print(length, k)
    subs = []
    
    # s = 0
    # q = k
    # while True:
    #     if q > length: 
    #         subs.append(string[s:])
    #         break
    #     subs.append(string[s:q])
    #     s = q
    #     q+=q
    
    q = k
    s, i = 0, 1
    while True:
        # print(s, q)
        if q > length:
            subs.append(string[s:])
            break
        subs.append(string[s:q])
        s = q
        q += k
    
    # print(subs)
    for s in subs:
        ns = ''
        for c in s:
            if c in ns: continue
            else: ns+=c
        print(ns)

if __name__ == '__main__':
    # string, k = input(), int(input())
    # string = 'AABCAAADA'
    # k=3
    i = 0
    lines = sys.stdin.readlines()
    while i < len(lines):
        string= lines[i].strip()
        i+=1
        k= int(lines[i].strip())
        
        i+=1
        
        merge_the_tools(string, k)
        print()