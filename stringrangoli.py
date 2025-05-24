import string
def print_rangoli(size):
    result_list=[]
    for i in reversed(range(size)):
        char_list=[]
        for j in range(size-i):
            char_list.append(string.ascii_lowercase[i+j])
            char_ele= "" if(i==size-1 and j==0) else "-"
        result_list.append("-".join(reversed(char_list))[:-2]+char_ele+"-".join(char_list))

    elewidth = len(result_list[-1])

    result_list = result_list+result_list[-2::-1]

    result_list= [i.center(elewidth,"-") for i in result_list]
    print("\n".join(result_list))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


