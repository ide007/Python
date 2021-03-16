if __name__ == '__main__':
    import os

    new_project_name = 'new_project'

    def project_folders_creator(new_project_name):

        sub_folders = ['setting', 'mainapp', 'adminapp', 'authapp']

        if not os.path.exists(new_project_name):
            for sub_folders in sub_folders:
                os.makedirs(os.path.join(new_project_name, sub_folders))
            print('Стартер для проекта успешно создан.')


project_folders_creator(new_project_name)
