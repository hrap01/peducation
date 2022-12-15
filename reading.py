def read_from_file(path_to_file):
    f = open(path_to_file, 'r')
    data = ''
    try:
        raise TypeError("naše zkouška")
        data = f.read()
    except:
        print('error reading file')
        #return ''
    finally:
        f.close()
    return data

# def square_number(number):
#     a = int(number) * int(number)
#     return a

b = read_from_file('data.txt')
print (b)

#print(square_number(b))

