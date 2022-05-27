print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = list(name1)
name2 = list(name2)
true = ['t', 'r', 'u', 'e']
love = ['l', 'o', 'v', 'e']


def calc_love_helper(name):
    res1 = 0
    res2 = 0
    for i in range(len(name)):
        if name[i].lower() in love:
            res1 += 1
        if name[i].lower() in true:
            res2 += 1
    return res1, res2


a, b = calc_love_helper(name1)
c, d = calc_love_helper(name2)

print(a+c, b+d)