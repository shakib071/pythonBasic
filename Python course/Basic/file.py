# .csv comma seperated value
# .txt text file

# with open('massage.txt','w') as file: #write as file
#     file.write('I love you,python')

with open('massage.txt','r') as file: #massage nam change kora jacche na
    text=file.read()
    print(text)