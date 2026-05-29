# ----------------------------
# KNOWLEDGE BASES
# ----------------------------

tourist_places = {

    "Goa":{

        "type":"Beach",

        "budget":25000,

        "food":"Seafood",

        "days":3
    },

    "Jaipur":{

        "type":"Heritage",

        "budget":18000,

        "food":"Rajasthani",

        "days":2
    },

    "Manali":{

        "type":"Mountain",

        "budget":22000,

        "food":"North Indian",

        "days":4
    },

    "Hyderabad":{

        "type":"Food",

        "budget":15000,

        "food":"Biryani",

        "days":2
    }

}


food_database = {

    "Vegetarian":[

        "Paneer Curry",

        "Dosa",

        "Veg Meals"

    ],

    "NonVegetarian":[

        "Chicken Curry",

        "Seafood",

        "Biryani"

    ]
}


transport_cost = {

    "Goa":5000,

    "Jaipur":3500,

    "Manali":4500,

    "Hyderabad":2500
}


hotel_cost_per_day = {

    "Goa":2500,

    "Jaipur":1800,

    "Manali":2200,

    "Hyderabad":2000
}


# ----------------------------
# USER INPUT
# ----------------------------

budget = int(

    input("Enter Budget: ")

)

interest = input(

    "Interest (Beach/Heritage/Mountain/Food): "

)

food_pref = input(

    "Food Preference (Vegetarian/NonVegetarian): "

)

days = int(

    input("Days: ")

)


# ----------------------------
# RECOMMEND DESTINATION
# ----------------------------

recommendations=[]

for place,data in tourist_places.items():

    if(

        data["type"].lower()==interest.lower()

        and

        data["budget"]<=budget

    ):

        recommendations.append(place)


if len(recommendations)==0:

    print(

        "\nNo suitable destinations"

    )

    exit()


destination = recommendations[0]


# ----------------------------
# COST ESTIMATION
# ----------------------------

transport = transport_cost[destination]

hotel = hotel_cost_per_day[destination]*days

food_cost = days*1000

total = transport+hotel+food_cost


# ----------------------------
# ITINERARY GENERATION
# ----------------------------

print("\n===== TRAVEL PLAN =====")

print(

    "Destination:",

    destination
)

print(

    "Suggested Food:",

    food_database[food_pref]
)

print(

    "Estimated Cost:",

    total
)

print("\nItinerary:\n")


for d in range(1,days+1):

    print(

        "Day",

        d,

        ": Visit",

        destination,

        "Attractions"

    )


print(

    "\nTrip Planning Complete!"
)
