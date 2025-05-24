def count_substring(string, sub_string):
    count = 0
    last_found = 0
    for init in range(0, len(string)):
        last_found = string.find(sub_string, last_found+1)
        if(init) != -1:
            count+=1
        else:
            break
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)