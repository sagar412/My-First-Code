# Reading the files, c10p1
with open('learning_python.txt') as File1:
    contents = File1.read()
    print(contents.rstrip())
    for line in File1:
       print(line.rstrip())
