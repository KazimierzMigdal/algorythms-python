def bubble_sort(list):
    lenght = len(list)-1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(lenght):
            if list[i]>list[i+1]:
                sorted = False
                list[i], list[i+1] = list[i+1], list[i]
    return list
