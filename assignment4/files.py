try:
    #opening the file and reading
    file1 = open('sample.txt', 'r')
    reading_file = file1.read()
    print(reading_file)
    file1.close()
    #if the file is not found error is shown
except FileNotFoundError: 
<<<<<<< HEAD
    print("Error: The file was not found. Please check the file path and try again.")
=======
    print("Error: The file was not found. Please check the file path and try again.")
>>>>>>> 63f6c3b16b240f941bf6099701cbfea593000359
