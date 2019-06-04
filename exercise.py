[
  [None, "Pumpkin", None, None],
  ["Socks", nil, "Mimi", None],
  ["Gismo", "Shadow", None, None],
  ["Smokey","Toast","Pacha","Mau"]
]

def available_seats():
    r = 0
    for row in seating:
        r+=1
        s=0
        if seat == None:
            print(f"Row {r} seat {s} is free. Do you want to sit there? (y/n)")
            answer = input()
            if answer == 'y':
                print("What is your name")
                name = input()
                del row[s-1]
                row.insert(int(s)-1, name)
                print(f"Please sit in row {r}, seat {s}.")
                return
            else: 
                pass

available_seats()
print(seating)