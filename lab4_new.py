import time

eventsList = [
    (1991, "Declaration of Independence of Ukraine"),
    (1994, "Ukraine becomes a member of the Partnership for Peace program"),
    (2004, "Orange Revolution in Ukraine"),
    (2013, "Euromaidan protests and subsequent revolution"),
    (2014, "Annexation of Crimea by the Russian Federation"),
    (2022, "Russian invasion of Ukraine"),
]

toVisit = [1991, 2004, 2011, 2013]
eventsDict = {year: event for year, event in eventsList}


def addEvent(year, description):
    eventsList.append((year, description))
    eventsDict[year] = description


def deleteEvent(year):
    eventsDict.pop(year)


def teleport_to_event(year):
    try:
        event = eventsDict[year]
        print(f"You have been teleported sucsessfully to {year}. Event: {event}.")
    except KeyError:
        print(f"Error: {year} is missing in dictionary of events.")


def show_events():
    for year in eventsDict:
        print(f"{year} - {eventsDict[year]}")


def interactiveMenu():
    while True:
        print(
            "What do you want to do? 1 - Show events, 2 - Teleport to events, 3 - Add event, 4 - Delete Event, 5 - Exit"
        )
        ch = int(input("Enter number: "))
        match ch:
            case 1:
                show_events()
            case 2:
                for year in toVisit:
                    teleport_to_event(year)
                    time.sleep(3)
            case 3:
                input_year = int(input("Enter year to add: "))
                input_desc = input("Enter description to add: ")
                addEvent(input_year, input_desc)
            case 4:
                input_year = int(input("Enter year to remove: "))
                try:
                    deleteEvent(input_year)
                except KeyError:
                    print("This year isn't exist yeat")

            case 5:
                break


interactiveMenu()
