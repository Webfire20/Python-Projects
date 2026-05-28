import pickle
stu=0
file=open("stu.txt", "ab+")
found=False
try:
    while True:
        rpos=file.tell()
        stu=pickle.load(file)
        if stu['Marks']> 81:
            stu['Marks']+=2
            file.seek(rpos)
            found=True
except EOFError:
    if found == False:
        print("No record found!")
    else:
        print("successful")
