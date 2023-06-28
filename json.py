import json


employees = [
    {
        "Name": "John Doe",
        "DOB": "1990-05-15",
        "Height": 175,
        "City": "New York",
        "State": "New York"
    },
    {
        "Name": "Jane Smith",
        "DOB": "1988-09-20",
        "Height": 162,
        "City": "Los Angeles",
        "State": "California"
    },
    {
        "Name": "Mike Johnson",
        "DOB": "1995-03-10",
        "Height": 180,
        "City": "Chicago",
        "State": "Illinois"
    },
    {
        "Name": "Emily Davis",
        "DOB": "1992-12-05",
        "Height": 168,
        "City": "Houston",
        "State": "Texas"
    },
    {
        "Name": "David Brown",
        "DOB": "1991-07-18",
        "Height": 170,
        "City": "Miami",
        "State": "Florida"
    }
]


with open("employee.json", "w") as file:
    json.dump(employees, file, indent=4)



import json


indian_states = {
    "Andhra Pradesh": "Hyderabad",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Gujarat": "Gandhinagar",
    "Karnataka": "Bengaluru",
    "Maharashtra": "Mumbai"
}


with open("indian_states.json", "w") as file:
    json.dump(indian_states, file, indent=4)

print(employees)