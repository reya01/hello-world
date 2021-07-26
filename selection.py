def selection_sort(list1):
    counter = 0
    updated_list = []
    
    while len(list1) > 0:
        low_value = list1[0]
        low_index = 0

        for i in range(0, len(list1)):
            if list1[i] < low_value:
                low_index = i
                low_value = list1[i]
        updated_list.append(low_value)
        list1.pop(low_index)
        
    return updated_list
    
    
def main():
    list_to_sort1 = [11, 9, 17, 5, 12, 999, -11111, 101, 11, 99, 101.1]
    list_to_sort2 = [41, 12, 12, 11, 13, 999, 999, -11111, 104, 777, 9679, 1011.1, 42, 45, 45, 66, 79, 111111, 1010101010, 10, 0, 0]
    print(selection_sort(list_to_sort1))
    print(selection_sort(list_to_sort2))

main()