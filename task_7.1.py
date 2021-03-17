if __name__ == '__main__':
    import os

    sub_folders = ['setting', 'mainapp', 'adminapp', 'authapp']


    def project_folders_creator(new_project_name):
        if not os.path.exists(new_project_name):
            for sub_folder in sub_folders:
                os.makedirs(os.path.join(new_project_name, sub_folder))
            print('Стартер для проекта успешно создан.')


    project_folders_creator('new_project')
