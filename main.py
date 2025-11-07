from collections import Counter

def text_analysis(text):
    # 统计每个字符的出现频率
    char_counter = Counter(text)
    # 按频率降序排序（频率相同则按字符升序）
    sorted_chars = sorted(char_counter.items(), key=lambda x: (-x[1], x[0]))
    # 打印结果
    for char, freq in sorted_chars:
        print(f"字符 '{char}' 出现频率：{freq}")

# 调用函数（示例）
if __name__ == "__main__":
    input_text = input("请输入要分析的字符串：")
    text_analysis(input_text)
