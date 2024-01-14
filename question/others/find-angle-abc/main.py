import sys
import math

def find_angle_mbc(ab: int, bc: int) -> None:
    
    degree = round(math.degrees(math.atan(ab/bc)))
    print(f"{degree}{chr(176)}")
    
if __name__ == "__main__":
    
    i = 0
    lines = sys.stdin.readlines()
    while i < len(lines):
        ab = int(lines[i].strip())
        i+=1
        bc = int(lines[i].strip())
        
        i+=1
        
        find_angle_mbc(ab, bc)