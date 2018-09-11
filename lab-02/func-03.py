


# Check if filename is less < 4
def myfunc(filename,nlines):
    if filename < 4:
        return "error"

    with open(filename) as f:
        lines = f.readlines()

    my_lines = lines[:nlines]

    with open('myfiles.txt','w') as f:
        for line in my_lines:
            f.write(line)

myfunc("functions.py",3)


