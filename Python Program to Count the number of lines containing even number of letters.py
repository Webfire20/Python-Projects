def count(path): 
    evenLines=0
    with open(path, 'r') as fp:
        lines = fp.readlines()
        for line in lines:
            if len(line)%2==0:
                evenLines+= 1
        return evenLines
path='RobertFrost-Road Not Taken.txt'
no_of_lines=count(path)
print('The Number of Lines with Even Number of Letters are: ',no_of_lines)
