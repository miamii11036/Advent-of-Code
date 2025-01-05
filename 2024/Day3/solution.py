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