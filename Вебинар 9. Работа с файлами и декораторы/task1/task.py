from pathlib import Path

work_dir = Path.cwd()
path_to_input = Path("test_file/task1_data.txt")
path_to_output = Path("test_file/task1_answer.txt")
abs_path_input = Path(work_dir, path_to_input)
abs_path_output = Path(work_dir, path_to_output)
content_list = [] # список строк
position = 0 # бегунок для пересбора получившегося списка

with open(abs_path_input, mode='r', encoding='utf-8') as f_in:

    for line in f_in.readlines():
        content_list.append(line)

    for lines in content_list:
        line_to_str = str(lines).replace("]",'').replace("[",'').replace('\'','')
        for char in line_to_str:
            if char.isdigit():
                line_to_str = line_to_str.replace(char, '')
        content_list.insert(position, line_to_str) # меняем исходную строку на модифицированную
        content_list.pop(position+1)
        position += 1

with open(abs_path_output, mode='w', encoding='utf-8') as f_out:
    for i in content_list:
        f_out.writelines(i)