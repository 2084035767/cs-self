import os
import re

folder_path = "./"

def delete_text_in_files1(folder_path):
    # 获取文件夹下所有md文件的路径
    md_files = [file for file in os.listdir(folder_path) if file.endswith(".md")]

    for file in md_files:
        file_path = os.path.join(folder_path, file)
        with open(file_path, "r",encoding="utf8") as f:
            content = f.read()

        # 使用正则表达式匹配目标文本所在的段落，并删除该段落
        pattern1 = r"### 好消息([\s\S]*)！"
        updated_content1 = re.sub(pattern1, "", content, flags=re.DOTALL)
        # 将更新后的内容写回文件
        with open(file_path, "w",encoding="utf8") as f:
            f.write(updated_content1)

def delete_text_in_files2(folder_path):
    # 获取文件夹下所有md文件的路径
    md_files = [file for file in os.listdir(folder_path) if file.endswith(".md")]

    for file in md_files:
        file_path = os.path.join(folder_path, file)
        with open(file_path, "r",encoding="utf8") as f:
            content = f.read()

        # 使用正则表达式匹配目标文本所在的段落，并删除该段落
        pattern2 = r"### 其他([\s\S]*)e"
        updated_content2 = re.sub(pattern2, "", content, flags=re.DOTALL)
        # 将更新后的内容写回文件
        with open(file_path, "w",encoding="utf8") as f:
            f.write(updated_content2)


delete_text_in_files1(folder_path)
delete_text_in_files2(folder_path)