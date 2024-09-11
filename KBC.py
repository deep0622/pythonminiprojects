a = [
    ["how to become a millionaire", "trading", "business", "sellers", "bitcoins", "none", 2],
    ["how to become a millionaire", "trading", "business", "sellers", "bitcoins", "none", 4],
    ["how to become a millionaire", "trading", "business", "sellers", "bitcoins", "none", 1],
    ["how to become a millionaire", "trading", "business", "sellers", "bitcoins", "none", 3],
    ["wich car you drive", "Gwegon", "lembo", "RR","Ferari", "none" ,1 ],
    ["wich car you drive", "Gwegon", "lembo", "RR","Ferari", "none" ,4 ],
    ["wich car you drive", "Gwegon", "lembo", "RR","Ferari", "none" ,2 ],
    ["wich car you drive", "Gwegon", "lembo", "RR","Ferari", "none" ,3 ],
]

levels = [1000,2000,3000,5000,10000,20000,50000,80000,100000,500000,1000000,500000,10000000]
money = 0
for i in range(0,len(a)):
    qustion = a[i]

    print(f"\n\nQuestion for rs. {levels[i]}")
    print(f" A. {qustion[1]}               B. {qustion[2]}")
    print(f" c. {qustion[3]}               D. {qustion[4]}")
    reply =int(input("enter your answer (1 to 4) or 0 to quit: "))
    if reply ==0:
        money = levels[i-1]
        break
    if (reply == qustion[-1]):
        print(f"correct answer,you have won Rs. {levels[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 50000
        elif i == 13:
            money = 500000
        elif i == 17:
            money = 1000000
    else:
        print("wrong answer!!")
        break

print(f"you take home money is {money}")