

class String:
    def __init__(self, s) -> None:
        self.s = s
        self.s_len = len(s)
        
    def sub_strings(self) -> list[str]:
        sub_string_list = []
        # Pick starting point
        for Len in range(1,self.s_len + 1):
            
            # Pick ending point
            for i in range(self.s_len - Len + 1):
                
                # Print characters from current
                # starting point to current ending
                # point. 
                j = i + Len - 1
                ts = ''
                for k in range(i,j + 1):
                    # print(s[k], end="")
                    ts = ts + s[k]
                if ts not in sub_string_list:
                    sub_string_list.append(ts)
        return sub_string_list
        # lista=[]
        # [lista.append(s[i:i+k+1]) for i in range(len(s)) for k in range(len(s)-i) if s[i:i+k+1] not in lista and s[i:i+k+1][::-1] not in lista]
        # return lista
    
    def get_occurence(self, subs: str) -> int:
        marker = 0
        count = 0
        while marker < len(self.s):
            try:
                # print(s.index(subs,marker))
                marker = self.s.index(subs, marker) + 1
                count += 1
            except ValueError:
                break
                # print("String not found")
                # marker = len(s)
        return count

class Stuart:
    name: str = "Stuart"
    point: int = 0
    def __str__(self): return f"{self.name} {self.point}"
    
class Kevin:
    name: str = "Kevin"
    point: int = 0
    def __str__(self): return f"{self.name} {self.point}"

def minion_game(string):
    string_class: String = String(string)
    string_class.s = string
    kevin: Kevin = Kevin()
    stuart: Stuart = Stuart()
    

    vowels = ['a', 'e', 'i', 'o', 'u']
    # sub_strings_list = list(set(string_class.sub_strings(string, len(string))))
    sub_strings_list = string_class.sub_strings()
    # print(sub_strings_list)
    

    for s in sub_strings_list:
        if s[0].lower() in vowels:
            # print(s, string.count(s))
            kevin.point += string_class.get_occurence(s)
        else:
            
            # print(s, string_class.get_occurence(s))
            stuart.point += string_class.get_occurence(s)
    
    if kevin.point == stuart.point:
        print("Draw")
    elif kevin.point > stuart.point:
        print(kevin)
    else:
        print(stuart)


def minion_game_2(string):
    vowels = 'AEIOU'
    Stuart_score, Kevin_score = 0, 0
    length = len(string)
    for start_idx in range(length):
        score = length - start_idx
        print(length, start_idx, string[start_idx])
        if string[start_idx] in vowels:
            Kevin_score += score
        else:
            Stuart_score += score
    if Stuart_score == Kevin_score:
        print('Draw')
    if Stuart_score > Kevin_score:
        print('Stuart {}'.format(Stuart_score))
    if Stuart_score < Kevin_score:
        print('Kevin {}'.format(Kevin_score))

if __name__ == '__main__':
    # s = input()
    s = "BANANA"

    minion_game_2(s)