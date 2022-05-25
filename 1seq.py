var_range=int(input("Введите количество элементов будущего списка "))
lst_nums=[]
for i in range(0,var_range):
    lst_nums.append(input("Введите число: "))
lst_nums.sort()
print(lst_nums)