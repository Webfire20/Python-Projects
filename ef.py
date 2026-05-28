def lenwords(str):
    word=str.split()
    leng=[]
    for i in word:
        length=len(word)
        leng.append(length)
    x = tuple(leng)
    print(x)
lenwords('Ok its very much good')        
    
