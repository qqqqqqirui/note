class ExceedanceError:
    def __init__(self, code, message):
        self.code=code
        self.message=message
    def __str__(self):
        return f"{self.code}:{self.message}"


nums=list(map(int, input("please enter 4 numbers between 100 and 999 seperated by space:").split(" ")))
l=[]
for i in nums:
    if i>999:
        raise ExceedanceError(i, "exceeds 3 digits")
    elif i**(1/2)!=round(100**(1/2)) and i%3==0 and i%2!=0:
        l.append(i)
if l:
    print(max(l))
else:
    print("There is no such number")







































