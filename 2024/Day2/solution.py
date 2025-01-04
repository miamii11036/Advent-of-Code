
def read_txt(file):
    """
    讀取.txt文件
    """
    try:
        with open(file, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print("檔案不存在")
        exit()
    except Exception as e:
        print(f"讀取時發生錯誤：{e}")
        exit()

def process_data(data):
    """
    將字串轉成串列，計算每個一維串列中兩兩元素相減的結果，輸出二維串列
    """
    data_list = [line.split() for line in data]
    subtract = []
    for row in data_list:
        sub = [int(row[j]) - int(row[j-1]) for j in range(len(row) - 1, 0, -1)]
        subtract.append(sub)
    return subtract

def filter_data(data):
    """
    過濾出每個一維串列中元素皆>0 或 < 0，且元素值在-3~3之間的一維串列
    inpit:二維串列
    output:二維串列
    """
    return [i for i in data if (all(value > 0 for value in i) or all(value < 0 for value in i)) and 
            (all(-3 <= value <= 3 for value in i))]

# data = read_txt("clue.txt")
# process = process_data(data)
# answer = filter_data(process)
# print(len(answer)) #answer1
    
def safe_data(row): 
    substrate = []
    for i in range(len(row)-1):
        substrate.append(int(row[i+1]) - int(row[i]))

    positive = all(1 <= diff <= 3 for diff in substrate)
    negative = all(-3 <= diff <= -1 for diff in substrate)
    return positive or negative

def also_safe_after_removed(row):
    for i in range(len(row)):
        modify = row[:i] + row[i+1:]
        if safe_data(modify):
            return True
    return False

def count_safe_data(data):
    count = 0
    data_list = [line.split() for line in data]
    for row in data_list:
        if safe_data(row) or also_safe_after_removed(row):
            count += 1
    return count
            
data = read_txt("clue.txt")
safe_count = count_safe_data(data)
print(safe_count) #answer2
