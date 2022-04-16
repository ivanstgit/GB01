# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные исключительные ситуации;
# это реальная задача, которая решена, например, во фреймворке django.
import os
import shutil

TEMPLATES_DIR_NAME = 'templates'

root_dir = 'my_project'
tgt_root_dir = os.path.join(root_dir, TEMPLATES_DIR_NAME)

# clear path
if os.path.exists(tgt_root_dir):
    try:
        shutil.rmtree(tgt_root_dir)
    except Exception as e:
        print(f'directory {tgt_root_dir} erasing error:{e}')
        exit(1)

# fill path
for root, dirs, files in os.walk(root_dir):
    rel_path = os.path.relpath(root, root_dir)
    path_list = os.path.split(rel_path)
    leaf_folder = path_list[-1]
    top_folder = path_list[0]
    # print(root, rel_path, top_folder, leaf_folder, dirs, files)
    if leaf_folder == TEMPLATES_DIR_NAME and top_folder != TEMPLATES_DIR_NAME:
        if len(dirs):
            tgt_path = os.path.join(root_dir, TEMPLATES_DIR_NAME, dirs[0])
            if not os.path.exists(tgt_path):
                try:
                    os.makedirs(tgt_path)
                except Exception as e:
                    print(f'directory {tgt_path} creation error:{e}')
                    exit(1)
            src_path = os.path.join(root, dirs[0])
            html_files = [os.path.join(src_path, item.name)
                          for item in os.scandir(src_path)
                          if item.name.endswith('.html')]
            for file in html_files:
                shutil.copy(file, tgt_path)
