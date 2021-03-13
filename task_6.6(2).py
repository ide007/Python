from sys import argv


def bakery_in_out(argv):
    with open('bakery.csv', 'a', encoding='utf-8') as input_chek:
       with open('bakery.csv', encoding='utf-8') as output:
           if len(argv) > 1 and [i for i in argv[1:] if i.replace('.', '').isdigit()]:
               if len(argv) == 3:
                   print(*output.read(). split()[int(argv[1]) - 1: int(argv[2])], sep='\n')
               if ',' in argv[1] or '.' in argv[1]:
                   output.read()
                   print(argv[1], file=input_chek)
               else:
                   print(*output.readlines()[int(argv[1]) - 1:], sep='')
           else:
               print(output.read())


if __name__ == '__main__':
    bakery_in_out(*argv[1:])
