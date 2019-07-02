list_number = [1,23,45,2,4,1,23,45,23,99,56]
final_list = []
duplicate_list = []

print('List Number :', list_number)
print('\nDuplicate List')
for num in list_number:
    if num not in final_list: 
        final_list.append(num)
    elif num in final_list:
        if num not in duplicate_list:
            duplicate_list.append(num)    
            print(num)

print('\nNot a Duplicate List')
for num in final_list:
    if num not in duplicate_list: 
        print(num)

