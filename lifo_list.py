import random

k = random.randrange(10,20)
print(k," no. of students submitted assignment")
v = random.sample(range(1, 100), k)
print(v)
print("these are roll numbers of students who submitted assignment in order of submission")

while(len(v)>10):    #pop until only 10 remain, these will be the first 10
    v.pop()

print(v)
print("these are roll numbers of first Ten students who submitted assignment")

