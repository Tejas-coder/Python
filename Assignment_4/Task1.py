try:
    file = open('Assignment_4/sample.txt', 'r')
    data = file.read()
    data = data.split('\n')
    print('Line 1: {}'.format(data[0]))
    print('Line 2: {}'.format(data[1]))
    file.close()
except FileNotFoundError:
    print("File Not Found!")

