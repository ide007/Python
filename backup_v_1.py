import os
import time

source = ['E:\\WEB\\Linux', 'E:\\Python']
target_dir = 'E:\\Backup'
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = 'zip -qr {0} {1}'.format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Backup complete in ', target)
else:
    print('Some think wrong!. BACKUP NOT COMPLETE!!!!!')
