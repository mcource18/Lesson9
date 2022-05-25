str_nums_1=input("Введите элементы 1-го списка через запятую: ")
str_nums_2=input("Введите элементы 2-го списка через запятую: ")
int_lst_1=[int(i) for i in str_nums_1.split(",")]
int_lst_2=[int(i) for i in str_nums_2.split(",")]
print(list(set(int_lst_1)-set(int_lst_2)))