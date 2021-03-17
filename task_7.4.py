if __name__ == '__main__':
    import os

    path = os.path.abspath(os.getcwd())
    folder = 'some_data'
    fullPath = os.path.join(path, folder)
    my_dict = {}


    def dict_cr(key):
        if key in my_dict:
            my_dict[key] += 1
        else:
            my_dict[key] = 1


    def counter():
        for file in os.listdir(fullPath):
            fp = os.path.join(fullPath, file)
            size = int(os.path.getsize(fp))
            i = 10
            while (size // i) > 10:
                i *= 10
            dict_cr(i)

    counter()
    print(my_dict)
