import numbers
import random
 
def dice():
     number = random.randint(1, 6)
     return number
print(dice()) # 1から6の整数をランダムに出力する