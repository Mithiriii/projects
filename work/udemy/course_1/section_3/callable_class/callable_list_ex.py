class NoDuplicates:

    def __init__(self):

        self.list = []

    def __call__(self, new_items):

        for a in new_items:
            if not a in self.list:
                self.list.append(a)


my_no_dup_list = NoDuplicates()
print(my_no_dup_list.list)

my_no_dup_list(['keyboard', 'mouse'])
print(my_no_dup_list.list)

my_no_dup_list(['keyboard', 'mouse', 'pendrive'])
print(my_no_dup_list.list)

my_no_dup_list(['charger', 'pendrive'])
print(my_no_dup_list.list)