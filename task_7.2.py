import os

start_location = r'E:\Python'
project_name = 'Project'
pattern = ['setting',
           ['__init.py', 'dev.py', 'prod.py']]#, ['mainapp', ['__init.py',  'models.py', 'views.py'],
           # ['templates',
           #  ['mainapp', ['base.html', 'index.html']]]
           #  ], ['authapp',
           #  ['__init.py', 'models.py', 'views.py'],
           #  ['templates',
           #   ['mainapp',
           #    ['base.html', 'index.html']]]
           #  ]


def creatFolders(path):
    if os.path.exists(path):
        os.mkdir(path)


def build(root, data):
    if data:
        for d in data:
            if '.' in d:
                with open(d, 'w', encoding='utf-8') as file:
                    file.write('')
            else:
                name = d[0]
                path = os.path.join(root, name)
                creatFolders(path)
                build(path, d[1])


fullPath = os.path.join(start_location, project_name)
creatFolders(fullPath)
build(fullPath, pattern)




# import os
# import yaml
#
# config = yaml.load(open('config.yaml'), Loader=yaml.Loader)
#
#
# def creat_folder(path):
#     if not os.path.exists(path):
#         os.makedirs(path)
#
#
# def builder(root, data):
#     if data:
#         for key, value in data:
#             name = key
#             path = os.path.join(root, name)
#             creat_folder(path)
#             if value == dict:
#                 builder(path, value)
#
#
# path = r'D:\Projects'
# new_project_name = 'project_name'
# fullPath = os.path.join(path, new_project_name)
#
# builder(fullPath, config)
