import os
import time

source = ['E:\\Python', 'E:\\WEB\\Linux']
target_dir = 'E:\\Backup'
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(today)
    print('Directory was created', today)

target = today + os.sep + now + '.zip'

zip_command = 'zip -qr {0} {1}'.format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Backup complete in ', target)
else:
    print('Some think wrong! Backup not complete')
