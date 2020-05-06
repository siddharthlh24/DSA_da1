print("wepage navigation, options are , bwd , new , fwd , disp ")
print("current site is google.com , forward and backward stacks are empty , fwd or bwd on empty stacks does nothing")

fwd = []       #initialized empty arrays
bwd = []

site_curr = "google.com"

def add_new(site):
    global site_curr
    bwd.append(site_curr)       #puts existing current site in bwd stack
    site_curr = site             # changes current site to entered adress
    disp()

def go_fwd():                      #pressing forward button
    if(len(fwd)>0):
        global site_curr
        bwd.append(site_curr)      #puts existing current site in bwd stack
        site_curr = fwd[-1]        #puts latest site from fwd stack as current site
        fwd.pop()                  # delets latest site from fwd stack
    disp()

def go_bwd():                      #pressing back button
    if(len(bwd)>0):
        global site_curr
        fwd.append(site_curr)      #puts existing current site in fwd stack
        site_curr = bwd[-1]        #puts latest site from bwd stack as current site
        bwd.pop()                  # delets latest site from fwd stack
    disp()

def disp():                        # displays both stacks and current site
    global site_curr
    print("backward stack : ",bwd)
    print("current site : ",site_curr)
    print("forward stack : ",fwd[::-1])

while True:
    inp = input("enter choice <<")
    if(inp == "bwd"):
        go_bwd()
    if(inp == "fwd"):
        go_fwd()
    if(inp == "disp"):
        disp()
    if(inp == "new"):
        entered_site = input("enter new site name <<")
        add_new(entered_site)