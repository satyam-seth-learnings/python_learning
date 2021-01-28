def is_palindrom(word):
    if word==word[::-1]:
        return True
    return False
print(is_palindrom("naman"))
print(is_palindrom("horse"))