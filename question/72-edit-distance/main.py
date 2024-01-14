class Solution:
    distance = 0
    def minDistance(self, word1: str, word2: str) -> int:
        print(word1, word2)
        word1_split = [x for x in word1]
        word2_split = [x for x in word2]
        print(word1_split, word2_split)
        self.convert(word1_split, word2_split)
        return self.distance
    
    def convert(self, w1: list[str], w2: list[str]):
        cindex = 0
        char_sequence_list = []
        k = 0
        while k < len(w2):
            char_sequence = []
            for i in range(k, len(w2)):
                for j in range(cindex, len(w1)):
                    print(k, i, j)
                    if w2[i] == w1[j]:
                        char_sequence.append(w2[i])
                        cindex = j
                        break
            char_sequence_list.append(char_sequence)
            k+=1
        print(char_sequence_list)
                
    
    def insert(self, word_arr: list[str], index: int) ->  True:
        if index > len(word_arr)-1:
            return False
        self.distance+=1
        return True
    
    def delete(self, word_arr: list[str], index: int) ->  True:
        if index > len(word_arr)-1:
            return False
        self.distance+=1
        return True
    
    def replace(self, word_arr: list[str], index: int) ->  True:
        if index > len(word_arr)-1:
            return False
        self.distance+=1
        return True
        
def main():
    s: Solution = Solution()
    # word1, word2 = "intention", "execution"
    word1, word2 = "horse", "ros"
    print("Distance: {}".format(s.minDistance(word1, word2)))


if __name__ == "__main__":
    main()