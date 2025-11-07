# 1. 接收用户输入
text = input("请输入要分析的字符串：")

# 2. 统计每个字符的出现次数（用字典存储）
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1  # 已有该字符，次数+1
    else:
        char_count[char] = 1   # 新字符，次数设为1

# 3. 按出现次数降序排序
# 把字典转换成列表，再用sorted排序
sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

# 4. 打印结果
print("字符出现频率（降序）：")
for char, num in sorted_chars:
    print(f"字符 '{char}' 出现了 {num} 次")
