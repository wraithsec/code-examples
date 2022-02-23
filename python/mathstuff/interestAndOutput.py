#!/usr/bin/python3


def getComp(Prin,rate,time):
    New = Prin * ( 1.0 + rate ) ** (time)
    return New 

def getTotals(total):
    t = 0.0
    for i in total:
        t += i
    return t

def main():
    P = 12000.00
    r = 0.11
    t = 4.0
    print(f'Principal\tInterestRate\tYears')
    old = P
    total = []
    for i in range(0,4):
        new = getComp(P,r,i)
        total.append(new)
        print(f'{new:.2f}\t{r:.2%}\t\t{t:.0f}')
    print(f'=========')
    print(f'{getTotals(total):.2f}')
if __name__ == "__main__":
    main()


#12000.00
#13320.00
#14785.20
#16411.57
#56.516.77
