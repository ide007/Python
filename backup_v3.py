import os
import time

source = ['E:\\Python', 'E:\\WEB\\Linux']
target_dir = 'E:\\Backup'
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = input('Enter your comment for backup file--> ')
if len(comment) != 0:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'
else:
    target = today + os.sep + now + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Directory', today, 'was created.')

zip_command = 'zip -qr {0} {1}'.format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Backup complete in ', target)
else:
    print('Some think wrong! Backup not complete')
