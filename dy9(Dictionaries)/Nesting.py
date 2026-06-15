capitals = {
    "France":"Paris",
    "Germany":"Berlin",
}

# travel_log ={
#     "France":["Paris","Lille","Dijon"],
#     "Germany":["Stuttgart","Berlin"]
# }
#
# print(travel_log["France"][1])

nested_list = ["A", "B", ["C","D"]]

travel_log = {
    "France":{
        "num_times_visited": 8,
        "cities_visited":["Paris","Lyon","Marseille"]
    },
    "Germany":{
        "num_times_visited": 21,
        "cities_visited":["Dortmund","Stuttgart","Berlin"]
    },
}


print(travel_log["Germany"]["cities_visited"][2])