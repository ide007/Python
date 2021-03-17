if __name__ == '__main__':

    import os
    from shutil import copytree


    def copy_dir():
        source = 'my_project'
        dir_to_copy = 'templates'

        for root, dirs, files in os.walk(source):
            if root.find(dir_to_copy) > 0 and len(files) == 0:
                copytree(os.path.join(root), dir_to_copy, dirs_exist_ok=True)


    copy_dir()
    print('Копирование завершено')
