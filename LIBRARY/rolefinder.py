
def wrt(i):
    file = open(r'D:\Projects\CN\LIBRARY\role.txt','wt')
    file.write(str(i))
    file.close()

def rd():
    file = open(r'D:\Projects\CN\LIBRARY\role.txt','rt')
    x = file.read()
    return x
