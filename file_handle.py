f = open("batch.txt", "w")
f.write("This is a simple text writtento the file.\n")
f.close()
f=open("batch.txt","r")
with open("batch.txt", "w") as f:
    f.write("This is another sample \n")
    f.write("This is a simple text written to the file.\n")
    f.write("You can write multiple lines to the file using the write() method.\n")
    f.write("Make sure to close the file after writing to it.\n")
    f.write("This is the last line of the file.\n")
    f.write("You can also use the writelines() method to write multiple lines at once.\n")

    a="This is a sample text written to the file using the writelines."

    f.write(a)

    with open("batch.txt", "r") as f:
        content = f.read()
        print(content)  

        with open("batch.txt", "r") as f:
            for line in f:
                print(line.strip())

                with open("batch.txt", "r") as f:
                    f.write("\nThis line is appended to the file using 'append' mode.\n")
                    f.write("Appending allows you to add new content to the end of the file without overwriting existing data.\n")

                    with open("batch.txt", "r") as f:
                        f.read(10)
                        print(f.tell())

                        