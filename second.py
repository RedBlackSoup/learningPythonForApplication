import os

a = 1
print(a)
b = 2.33333
print(b)
s = "hellp day2!"
print(s)
#lt = list() # lt = []
lt = [a, b, s]
# lt[0] = a  
# lt[1] = b  
# lt[2] = s
print(lt)
lt.append(s) # lt = [a, b, s, s]
print(lt)
丁真 = "DingZhen"
lt.insert(1, 丁真) # lt = [a, 丁真, b, s, s]
print(lt)
lt2 = [1, 1, 4, 5, 1, 4]
lt.extend(lt2)
print(lt)
lt.append(lt2)
print(lt)

if b > 2: # if (condition):
    print("2 is miner than b")

if b > 2 and a == 0: # condition => or and
    print("b > 2 and a = 0")
else:
    print("i am using else")

if (not a == 0):# if a != 0:
    print("a != 0")

for i in lt:
    print(i)

for i in range(len(lt)):
    print(lt[i])

dic = dict() # dic = {}

dic = {"qsy":90, "dgl":100, "gaoge":66}
dic["qsy"] # 90
dic["dgl"] # 100
dic["gaoge"] # 66

# f(x) = 2x
# f(x, y) = x + y ^ 2
lt[i]
def isodd(obj):
    if type(obj) is int:
        if obj % 2 == 0:
            return True
        else:
            return False
    elif type(obj) is list:
        result = []
        for i in obj:
            if i % 2 == 0:
                result.append(i)
        return result
    return False

a_num = 100
a_lst = [1, 2, 4, 5, 6, 7 , 100]

if isodd(a_num):
    pass

print(isodd(a_lst))

def set_position(x, y):
    # put mouse into screen (x,y)
    pass

def click():
    # click
    pass

set_position(1000, 200)
for i in range(100):
    click()