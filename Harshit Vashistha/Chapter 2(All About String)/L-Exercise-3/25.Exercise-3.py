name,char=input("Enter comma separated name and character: ").split(",")
print(f"Length of your name is:{len(name)} ")
print(f"Character count :{(name.lower().count(char.lower()))}")