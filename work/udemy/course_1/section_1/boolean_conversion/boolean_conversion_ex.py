options = ['load data', 'export data', 'analyze & predict']
choice = 'load data'
while choice:
    for i, element in enumerate(options):
        print(i+1, ' ', element)
    choice = input('Select or above(enter):')
    if choice:
        try:
            choice_num = int(choice)
        except:
            print("It's not number")
            continue
        if 0 < choice_num < len(options):
            print(choice_num, options[choice_num-1])
        else:
            print("Out of scale")

