import collections

with open('nginx_log.txt', encoding='utf-8') as log:
    diction = collections.Counter()
    for i in log:
        i = i.split()[0]
        diction[i] +=1
    ip, count = diction.most_common(1)[0][0], dict.most_common(1)[0][1]
    print(f'Spammer {ip} - {count} times')
