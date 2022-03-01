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
    print("The % ratio for {} is {}".format(my_client, clients[my_client]))
except Exception as e:
    print("Sorry we have an error....\nDetails: {}".format(e))
else:
    print("The cost for {} is {}".format(my_client, clients[my_client]*total_cost))
finally:
    print("-= Calculation finished =-")