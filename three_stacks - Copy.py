list1 = [None] * 9  #taking default size as nine, can be changed

stackprops = [[ int(len(list1)/3-1) , 0 ],[ int(len(list1)/3) , int(2*len(list1)/3-1) ],[ int(2*len(list1)/3) , int(len(list1)-1) ]]
#beginning and end indices of stacks ( 2:0 3:5 6:8 if len(list1)==9 )

stcurr = [stackprops[0][0],stackprops[1][0],stackprops[2][0]]
# current indices of top in array

def prop_return(i):             # return beginning and end indices of chosen stack
    return stackprops[i-1]

def curr_return(i):         #return current index for chosen stack
    global stcurr
    return(stcurr[i-1])

def isFull(i):            # checks if chosen stack is full
    if(list1[prop_return(i)[1]]==None):
        return(False)
    else:
        return(True)

def isEmpty(i):               #checks if chose stack is empty
    if(list1[prop_return(i)[0]]==None):
        return(True)
    else:
        return(False)

def unit_stack_vector(i):       # defines in which direction stacking occurs  
    if(i==1):                   # for 1 we know it's left and 2 and 3,it is right
        return (-1)
    if(i==2 or i==3):
        return (1)

def index_mod_pos(i):           #modifies index during push
    global stcurr
    stcurr[i-1] += unit_stack_vector(i)

def index_mod_neg(i):           #modifies index during pop
    global stcurr
    stcurr[i-1] =stcurr[i-1] -  unit_stack_vector(i)

def Push(i,val):             #push into stack
    global stcurr,list1
    if(isFull(i)==False):
        list1[curr_return(i)]=val
        index_mod_pos(i)

def Pop(i):                     #pop from stack
    global stcurr,list1
    if(isEmpty(i)==False):
        index_mod_neg(i)
        list1[curr_return(i)]=None
        
# testbench begins here

print("list = ",list1)

Push(1,1)
print("after push in 1")
print(list1)

print("checking if stack 1 is empty or full" )
print(isEmpty(1))
print(isFull(1))

Push(1,2)
print("after push in 1")
print("list = ",list1)

Pop(1)
Push(3,3)
print("after pop in 1 and push in 3")
print("list = ",list1)