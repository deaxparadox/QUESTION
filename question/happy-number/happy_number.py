class Solution:
    def new_number(self, n: int) -> int:
        sum = 0
        while (n > 0):
            rem = n % 10
            n = n // 10
            sum = sum + rem * rem
        
        return sum

    def isHappy(self, n: int) -> bool:
        unique = set()
        status = True
        while (True):
            n = self.new_number(n)
            # print(n, end="\t")
            if (n == 1): break
            if n in unique:
                status = False
                break
            unique.add(n)
        # print()
        return status

                
# 



def main():
    s = Solution()
    for i in range(1, 20):
        print(f"{i}\t{s.isHappy(i)}")
    # i = 19
    # print(f"{i}\t{s.isHappy(i)}")

if __name__ == "__main__":
    main()