input1= input("enter some text here")

    #opening the file and reading
file1 = open('output.txt', 'w+')
writing_file = file1.write(input1)
file1.seek(0)
reading_file = file1.read()
print(reading_file)
file1.close()
