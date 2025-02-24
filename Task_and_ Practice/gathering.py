
# event = {
#     "Sports": [],
#     "DJ Night": [],
#     "Dance": [],
#     "Singing": [],
#     "Days": []
# }

# title = "Welcome to Aarambh 3.0 2025 by Indala Institute of Technology"
# print(title.center(100))
# print("-"*115)
# sub_title = "Join us for an exciting series of events. Participate and have fun!"
# print(sub_title.center(100, '-'))

# while True:
#     print("\n1. View Events")
#     print("2. Register for an Event")
#     print("3. View Registered Participants")
#     print("4. Exit")
    
#     choice = int(input("Enter your choice: "))
    
#     if(choice == 1):
#         print("\nEvents:")
#         for event in event:
#             print(f"- {event}")
    
#     elif(choice == 2):
#         name = input("Enter your name: ")
#         stu_class = input("Enter your class: ")
        
#         print("Select an event you want to participate: ")
#         event_list = list(event.keys())
#         for i, event in enumerate(event_list, 1):
#             print(f"{i}. {event}")
        
#         try:
#             event_choice = int(input("Enter the event number: "))
#             event_name = event_list[event_choice - 1]
#             event[event_name].append((name, stu_class))
#             print(f"\n{name} has been registered for {event_name}!\n")
        
#         except(IndexError, ValueError):
#             print("Invalid choice. Please try again.")

# events = {
#     "Science Fair": [],
#     "Art Competition": [],
#     "Coding Challenge": [],
#     "Debate Competition": []
# }

# print("\nWelcome to the School Event Registration!\n")
# print("Join us for an exciting series of events. Participate and have fun!\n")

# while True:
#     print("\n1. View Events")
#     print("2. Register for an Event")
#     print("3. View Registered Participants")
#     print("4. Exit")
    
#     choice = input("Enter your choice: ")
    
#     if choice == "1":
#         print("Upcoming Events:")
#         for event in events:
#             print(f"- {event}")
    
#     elif choice == "2":
#         name = input("Enter your name: ")
#         student_class = input("Enter your class: ")
        
#         print("Select an event to register:")
#         event_list = list(events.keys())
#         for i, event in enumerate(event_list, 1):
#             print(f"{i}. {event}")
        
#         try:
#             event_choice = int(input("Enter the event number: "))
#             event_name = event_list[event_choice - 1]
#             events[event_name].append((name, student_class))
#             print(f"\n{name} has been registered for {event_name}!\n")
#         except (IndexError, ValueError):
#             print("Invalid choice. Please try again.")
    
#     elif choice == "3":
#         print("\nRegistered Participants:")
#         for event, participants in events.items():
#             print(f"\n{event} - Total: {len(participants)}")
#             for name, student_class in participants:
#                 print(f"  - {name} (Class {student_class})")
    
#     elif choice == "4":
#         print("Thank you for participating! Goodbye!")
#         break
#     else:
#         print("Invalid choice, please try again.")

event ={
    "Sprots":[],
    "Dance": [],
    "Music": [],
}
print(event.keys())
event_list = list(event.keys())
print(event_list)

choose = input("Enter your choice: ")

if choose in event_list:
    print("True")
    event_list.append("Ram")
    print(event_list)
else:
    print("false")
