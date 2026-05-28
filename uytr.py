Consider = [10,4,2,7,8,1]
final=[]
def shift():
    for i in range(len(Consider) - 1):
        Consider[i] = Consider[i + 1]
        final.append(Consider[i])
    print(final)
shift()
