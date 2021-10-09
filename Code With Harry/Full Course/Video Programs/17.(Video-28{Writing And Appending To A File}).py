# f = open("17i.txt", "w")
# a = f.write("Harry bhai bahut achhe hain\n")
# print(a)
# f.close()

# f = open("17ii.txt", "a")
# a = f.write("Harry bhai bahut achhe hain\n")
# print(a)
# f.close()


# Handle read and write both
f = open("17ii.txt", "r+")
print(f.read())
f.write("thank you")