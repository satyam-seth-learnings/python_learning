# word count
def word_count(s):
    count={}
    for char in s:
        count[char]=s.count(char)
    return count
print(word_count("satyam"))