str_nums=input("Введите любые цифры через запятую: ")
int_lst=[int(i) for i in str_nums.replace(";",",").replace("/",",").split(",")]
dub_lst=set()
for num in int_lst:
    if int_lst.count(num)>1:
        dub_lst.add(num)

print(list(set(int_lst)-dub_lst))
