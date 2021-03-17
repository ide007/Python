if __name__ == '__main__':

    import yaml
    import os

    with open('config.yaml', encoding='utf-8') as f:
        conf = yaml.safe_load(f)


    def creater(values, prefix=''):
        for directory, paths in values.items():
            path_to_dir = os.path.join(prefix, directory)
            os.makedirs(path_to_dir, exist_ok=True)
            if isinstance(paths, dict):
                creater(paths, path_to_dir)
            else:
                for i in paths:
                    if isinstance(i, dict):
                        creater(i, path_to_dir)
                    elif isinstance(i, str):
                        with open(os.path.join(path_to_dir, f'{i}'), 'w') as file:
                            file.write('')


    creater(conf)
    print('Структура папок для проекта создана  в папке запуска скрипта.')
