# with open('nginx_log.txt', encoding='utf-8') as f:
#     for lin in f:
#         line = ((f.readline()).replace('"', ' ').replace(')"', '\n')).split()
#         _ = (line[0], line[5], line[6], '\n')
#         val = " ".join(map(str, _))
#         with open('log_for_6.1.txt', 'a', encoding='utf_8') as log:
#             log.write(val)
with open('nginx_log.txt', encoding='utf-8') as log:
    for lin in log:
        string = lin.replace('"', ' ').split()
        rez = (string[0], string[5], string[6])
        with open('rez_6.1.txt', 'a', encoding='utf-8') as r:
          r.write(str(rez) + '\n')

#with open('nginx_log.txt', encoding='utf_8') as log:
    # for lin in log:
    #     string = log.readline().split()
    #     rez = (string[0], string[5], string[6])
    #     print(type(rez), rez)
    # for lin in log:
    #     string = lin.split()
    #     rez = (string[0], string[5], string[6])
        #print(type(rez), rez)
    # for lin in log:
    #     string = lin.split()
    #     rez = (string[0], string[5][1:], string[6])
    #     with open('rez_6.1.txt', 'a', encoding='utf_8') as r:
    #         r.write(str(rez) + '\n')
