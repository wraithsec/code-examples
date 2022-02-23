#!/usr/bin/env python3
#LEARNING 
'''
Generators are special iterables that don't hold entire result in memory, yields one result at a time. 
So it hangs onto the input and calculates the output at the time we ask for it via next(genObj) or genObj.send(next).
At end of generator, stop iteration exception occurs. For loops can keep this from being a problem.
Value comes from if you have millions of values to iterate through that are a list.
    Since it doesn't hold all values in em and divies up one at a time.
Also when you exhaust it, you cant use it.
'''

def sq_nums(*nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

def gen_sq(*nums):
    for i in nums:
        yield (i*i)

alist = sq_nums(1,2,3,4) 
blist = [x*x for x in [5,6,7,8]]
agen = gen_sq(5,10,15,25)
bgen = (g*g for g in [10,20,30,40])

print(f"\nalist")
for i in alist:
    print(i)
print(f"\nblist")
for i in blist:
    print(i)
print(f"\nagen")
for i in agen:
    print(i)
print(f"\nbgen")
for r in bgen:
    print(r)
print(f"\nbgen casted to a list")
#You lose performance of genrators here. Also when exhausted, its done.
print(list(bgen))
bgen = (g*g for g in [10,20,30,40])
print(list(bgen))
