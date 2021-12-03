def splitString(s):
    return [ int(c) for c in s ]

def joinList(l):
    return ''.join(str(e) for e in l)

diagnostics = []
with open('input3.txt') as input:
    diagnostics = [ splitString(line.strip()) for line in input.readlines()]

def find_o2_nums(lst,bit):
    if len(lst) == 1:
        return lst[0]

    if bit >= len(lst[0]):
        print("Error: did not find a unique solution")
        return 

    list0 = []
    list1 = []
    sum_ = 0 
    for j in range(len(lst)):
        sum_ += lst[j][bit]
        if lst[j][bit] == 1:
            list1.append(lst[j])
        elif lst[j][bit] == 0:
            list0.append(lst[j])
        else:
            print("Error")
            print(lst[j][bit])

    if sum_ < len(lst)/2.:
        list1 = []
        if len(list0) == 0:
            print("Error: did not find any solution")
            return
        return find_o2_nums(list0,bit+1)
    else:
        list0 = []
        if len(list1) == 0:
            print("Error: did not find any solution")
            return
        return find_o2_nums(list1,bit+1)

def o2_rating(lst):
    return find_o2_nums(lst,0)

def find_co2_nums(lst,bit):
    if len(lst) == 1:
        return lst[0]

    if bit >= len(lst[0]):
        print("Error: did not find a unique solution")
        return 

    list0 = []
    list1 = []
    sum_ = 0 
    for j in range(len(lst)):
        sum_ += lst[j][bit]
        if lst[j][bit] == 1:
            list1.append(lst[j])
        elif lst[j][bit] == 0:
            list0.append(lst[j])
        else:
            print("Error")
            print(lst[j][bit])

    if sum_ >= len(lst)/2.:
        list1 = []
        if len(list0) == 0:
            print("Error: did not find any solution")
            return
        return find_co2_nums(list0,bit+1)
    else:
        list0 = []
        if len(list1) == 0:
            print("Error: did not find any solution")
            return
        return find_co2_nums(list1,bit+1)

def co2_rating(lst):
    return find_co2_nums(lst,0)

o2 = joinList(o2_rating(diagnostics))
co2 = joinList(co2_rating(diagnostics))

print("o2 = {}".format(o2))
o2int = int(o2,2)
print("co2 = {}".format(co2))
co2int = int(co2,2)
print("Life support rating = O2 x CO2 = {}".format(o2int*co2int))