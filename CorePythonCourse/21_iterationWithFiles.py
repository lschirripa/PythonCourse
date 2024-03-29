f = open("test.txt", mode = 'rt', encoding = 'utf-8')

for line in f:
    print(line)

f.close()


# i could use with-block, to avoid forgetting the close() function. The with-block can close all the resources that are currently open within the block

with open("test.txt", mode = "wt", encoding = 'utf-8') as f:
    f.writelines("this block allows me to forget closing")


# i could also use a try-finally block where in the finally block i can close the resources even though there is an error or an exception