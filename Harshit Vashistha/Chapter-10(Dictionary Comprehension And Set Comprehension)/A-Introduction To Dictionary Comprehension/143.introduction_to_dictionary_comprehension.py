# dictionary comprehension
# square={1:1,2:4,3:9}
square={num:num**2 for num in range(1,11)}
print(square)
square={num:num**2 for num in range(1,11)}
square1={f"Square Of {num} is":num**2 for num in range(1,11)}
print(square1)
for k,v in square1.items():
    print(f"{k}:{v}")
# word counting
string="Satyam"
word_count={char:string.count(char) for char in string}
print(word_count)