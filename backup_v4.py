import os
import time

source = ['E:\\WEB\\Linux', 'E:\\Python']
target_dir = 'E:\\Backup'
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
comment = input('Введите комментарий --> ')

if len(comment) != 0:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'
else:
    target = today + os.sep + now + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('каталог {0} успешно создан'.format(today))

zip_command = 'zip -qr {0} {1}'.format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в ', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
