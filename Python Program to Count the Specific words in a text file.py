def count_word(file_path,word): 
    with open(file_path,"r+") as file: 
        word_check=str(word) 
        text=file.read()
        text_list=text.split()
        count=0
        for i in text_list:
            if i.lower()==word_check:
                count += 1
        return count
        file.close()
wordtocount='the'
file='RobertFrost-Road Not Taken.txt'
print('The Total words are: ',count_word (file,wordtocount))
