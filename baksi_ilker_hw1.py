x: int
y: int
count: int = 0
replaceCount: int = 0
digits: list[int] = []
isNegative: bool = False
biggestDigit:int

def main() -> None:
    global x,y,digits
    validX()
    validY()
    toDigits(x)
    perform(digits,y)

def replaceAll(digits: list[int],y:int) -> list[int]:
    global replaceCount,biggestDigit
    replaceCount += 1
    if(replaceCount == 1 ): 
        biggestDigit = max(digits)
    if(replaceCount > len(digits)): return digits
    if(digits[replaceCount-1] == biggestDigit): digits[replaceCount-1] = y
    replaceAll(digits,y)
    return digits

def perform(digits: list[int],y:int) -> None:
    if(len(digits) % 2 == 0):
        digits = replaceAll(digits,y)
    else:
        frontList: list[int] = [y] * len(digits)
        digits = frontList + digits
    print(digits)

def toDigits(integer: int) -> None:
    global count,isNegative,digits
    if(count == 0 and integer == 0): digits = [0]
    count += 1
    if(integer == 0): return
    if (integer < 0): 
        integer *= -1
        isNegative = True
    digits.insert(0,integer%10)
    integer //= 10
    if(integer == 0 and isNegative):
        digits[0] = digits[0] * -1
        isNegative = False
    toDigits(integer)

def validX() -> None:
    global x  
    try:
        x = eval(input("Please enter x: "))
    except:
        print("Please enter a valid integer for x")
        validX()
    if(type(x) != int):
        print("Please enter a valid integer for x")
        validX()

def validY() -> None:
    global y
    try:
        y = eval(input("Please enter y: "))
    except:
        print("Please enter a valid integer for y")
        validY()
    if(y < -9 or y>9 or type(y)!= int):
        print("Please enter a 1-digit integer for y")
        validY()
        
main()
    