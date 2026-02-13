# 1
text1 = "men python o‘rganaman"
result1 = "-".join(text1.split())
print(result1)

# 2
text2 = "banana"
result2 = max(text2, key=text2.count)
print(result2)

# 3
text3 = "py3th0n9"
result3 = "".join([char for char in text3 if not char.isdigit()])
print(result3)

# 4
text4 = "level"
is_palindrome = text4 == text4[::-1]
print(is_palindrome)

# 5
text5 = "Men Python o‘rganaman"
result5 = " ".join(text5.split()[::-1])
print(result5)
