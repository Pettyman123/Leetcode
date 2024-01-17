j = int(input("The number of customers: "))
cost_i = 99



def cost_estimation():
    if n>=10 and n<20:
        cost_f = (cost_i* 0.9)*n
        print("After discount:{}$".format(cost_f *n))
    elif n>=20 and n<50:
        cost_f = (cost_i*0.8)*n
        print("After discount:{}$".format(cost_f *n))
    elif n>=50 and n<100:
        cost_f = (cost_i*0.7)*n
        print("After discount:{}$".format(cost_f *n))
    elif n>=100:
        cost_f = (cost_i*0.6)*n
        print("After discount:{}$".format(cost_f *n))

for i in range(j):
    n = int(input("The number of packages bought: "))
    print("The cost of package wihout discount:{}$".format(cost_i *n))
    cost_estimation()




