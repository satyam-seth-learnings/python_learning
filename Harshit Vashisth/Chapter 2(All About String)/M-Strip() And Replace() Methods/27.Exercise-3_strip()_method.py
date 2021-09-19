name,char=input("Enter comma separated name and character: ").split(",")
print(f"Length of your name is:{len(name.strip())} ")
print(f"Character count :{(name.strip().lower().count(char.strip().lower()))}") 