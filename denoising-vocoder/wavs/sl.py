import os
import random
import shutil

# 从a文件夹中随机选择15个文件
path_to_a='./apnet'
# path_to_b='./apnetpro'
path_to_c='../../datasets/dataset_se/testset_clean'
path_to_d='./gt'
# files_in_a = os.listdir(path_to_a)
# selected_files = random.sample(files_in_a, 15)

# # 复制选中的文件到b文件夹中
# for file in selected_files:
#     src = os.path.join(path_to_a, file)
#     dst = os.path.join(path_to_b, file)
#     shutil.copy(src, dst)
files_in_a = [f for f in os.listdir(path_to_a) if f.endswith('.wav')]

# 在c文件夹中找到同名文件并复制到d文件夹中
for file in files_in_a:
    src = os.path.join(path_to_c, file)
    if os.path.exists(src):
        dst = os.path.join(path_to_d, file)
        shutil.copy(src, dst)