def count_substring(string, sub_string):

    indexes = []

    next_index = string.find(sub_string) + len(sub_string)

    if next_index == -1:
        return -1
    
    while next_index != (-1 + len(sub_string)):
        indexes.append(next_index) 
        next_index = string.find(sub_string, int(next_index)) + len(sub_string)

    return len(indexes)

if __name__ == '__main__':
    string = input().strip().lower()
    sub_string = input().strip().lower()

    # print(string)
    # print(sub_string)
    
    count = count_substring(string, sub_string)
    print(count)

# far way better resolution

# def count_substring(string, sub_string):
#     count = 0
#     for i in range(len(string)):
#         if string[i:].startswith(sub_string):
#             count += 1
#     return count