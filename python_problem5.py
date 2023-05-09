def write_even_file(file):
    f = open(file)
    w = open("python_problem5_text.txt", "w")
    content = f.readlines()
    i = 1
    while i <= len(content):
        w.write(content[i])
        i += 2
file = "rosalind_ini5.txt"
print(write_even_file(file))