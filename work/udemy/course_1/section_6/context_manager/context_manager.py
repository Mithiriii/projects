import time


with open(r'c:\temp\my_file.txt', 'w+') as file:
    file.writelines("SUCCESS")


class time_measure:

    def __init__(self):
        pass

    def __enter__(self):
        print('entering...')
        self.__start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exiting...')
        self.__stop = time.time()
        self.__difference = self.__stop - self.__start
        print("Execution time: {}".format(self.__difference))


with time_measure() as my_timer:
    time.sleep(3)
