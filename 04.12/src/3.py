with open("example.txt", "w") as file:
    file.write("Hello world")


file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

with open("image.jpg", "rb") as source_file:
    with open("image_copy.jpg", "wb") as dest_file:
        dest_file.write(source_file.read())