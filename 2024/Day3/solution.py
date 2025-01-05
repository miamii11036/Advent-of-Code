import re 

def read_txt(file = "clue.txt"):
    try:
        with open(file, 'r', encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"讀取出問題:{e}")
        exit()

def extract_patterns(text):
    pattern = r"mul\(\d+,\d+\)"
    matches = re.findall(pattern,text)
    return matches

def removed_mul(data):
    keyword = "mul("
    keyword2 = ")"
    return data.replace(keyword, "").replace(keyword2,"")

def answer(data):
    answer = 0
    for value in data:
        modify_value = removed_mul(value)
        final_data = modify_value.split(",")
        answer += (int(final_data[0]) * int(final_data[1]))
    return answer

origin_data = read_txt("clue.txt")
# filter_data = extract_patterns(origin_data)
# Answer = answer(filter_data)
# print(Answer)


def filter_data(txt):
    mul_pattern = r"mul\((\d+),(\d+)\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    do_status = True
    total_sum = 0

    extract_data = re.finditer(f"{mul_pattern}|{do_pattern}|{dont_pattern}", txt)
    for value in extract_data:
        if value.group(1) and value.group(2):
            if do_status:
                x = int(value.group(1))
                y = int(value.group(2))
                total_sum += x * y
        elif value.group(0) == "do()":
            do_status = True
        elif value.group(0) == "don't()":
            do_status = False
    return total_sum

Answer2 = filter_data(origin_data)
print(Answer2)
