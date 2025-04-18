import os


def print_all_csv_filenames_with_index(path,work):
    print(f'———————————————————————{work}———————————————————————')
    try:
        # 获取目录下的所有文件
        files = os.listdir(path)
    except FileNotFoundError:
        print("❌ 文件夹路径无效。")
    # 过滤出CSV文件并排序（按文件名）
    csv_files = sorted([f for f in files if f.lower().endswith('.csv')])
    # 构建带序号的字典（从1开始）
    indexed_csv_dic = {i + 1: name for i, name in enumerate(csv_files)}
    print("序列号\t文件名")
    for i, j in indexed_csv_dic.items():
        print(str(i) + ':' + j)
    return indexed_csv_dic

def input_index(index_dic):
    product_index = input("(此项可不输入，默认从 首项 开始)\n请输入 序列号：").strip()
    try:
        product = index_dic[int(product_index)]
    except ValueError:
        product = index_dic[1]
        print("\nℹ️ 未输入 序列号，默认从首个开始。")
    except KeyError:
        print("\n❌ 未存在 该序列号。")
        exit()
    return product

def get_all_folder_names(path,work):
    print(f'———————————————————————{work}———————————————————————')
    try:
        # 获取所有条目（文件 + 文件夹）
        items = os.listdir(path)
        # 过滤出文件夹
        folders = [f for f in items if os.path.isdir(os.path.join(path, f))]
        folders_dict = {idx + 1: name for idx, name in enumerate(folders)}
        # 打印文件夹列表，带序号
        for idx, folder in folders_dict.items():
            print(f"{idx}: {folder}")

        return folders_dict

    except FileNotFoundError:
        print("❌ 路径不存在")
        exit()
