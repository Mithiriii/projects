clients = {
    "INFO": 0.5,
    "DATA": 0.2,
    "SOFT": 0.2,
    "INTER": 0.1,
    "OMEGA": 0.0
}

my_client = input("Enter client's name: ")
total_cost = 7200
try:
    ratio = float(input("Enter new ratio: "))
    print("The default % ratio for {} is {}, a new one is {}".format(my_client, clients[my_client], ratio))
    print("The cost for {} is {}".format(my_client, clients[my_client]*total_cost))
    print("The new ratio in comparison to old ratio: {}".format(clients[my_client]/ratio))
except KeyError as e:
    print("Client {} is not on the list {}. \nDetails:{}".format(my_client, [c for c in clients.keys()], e))
except ValueError as e:
    print("There is a problem with entered value for ratio - it must be a number. \nDetail: \n{}".format(e))
except ZeroDivisionError as e:
    print("The new ratio cannot be 0\nDetails:{}".format(e))
except Exception as e:
    print("Sorry we have an error....\nDetails: {}".format(e))
