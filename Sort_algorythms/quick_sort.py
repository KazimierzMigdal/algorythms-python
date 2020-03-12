def quick_sort(list):
    if len(list)<=1:
        return list
    else:
        smaler_list = []
        larger_list = []
        pivot = list.pop()
        for element in list:
            if element<=pivot:
                smaler_list.append(element)
            else:
                larger_list.append(element)
        return quick_sort(smaler_list)+[pivot]+quick_sort(larger_list)
