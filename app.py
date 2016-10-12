"""
Usage:
    create_room (Living|Office) <room_name>...
    add_person <person_name> (Fellow|Staff) [--accomodation=N]
    reallocate_person <employee_id> <new_room_name>
    load_people <filename>
    print_allocations [--o=filename]
    print_unallocated [--o=filename]
    print_room <room_name>
    save_state [--db=sqlite_database]
    load_state <sqlite_database>
    quit
    
Options:
    -h --help         Show this screen.
    -i --interactive  Interactive Mode
    --o --filename    Specify filename
    --db              Name of SQLite database
    --accommodation   If person needs accommodation [default='N']
"""

import cmd
from docopt import docopt, DocoptExit
from models.amity import Amity

amity = Amity()

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as exit:
            # Thrown when args do not match

            print("You have entered an invalid command!")
            print(exit)
            return

        except SystemExit:
            # Prints the usage for --help
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

def intro():
    print("WELCOME TO AMITY SPACE ALLOCATION!".center(70))
    print ("Allocate rooms to staff and fellows in Amity".center(70))
    print ("1. help".center(70))
    print ("2. quit".center(70))


class AmityInteractive(cmd.Cmd):
    prompt = 'Start>>>'

    # file = None

    @docopt_cmd
    def do_create_room(self, arg):
        """
        Create a room in Amity. A room can either be an office or living space.
        Create as many rooms as possible by specifying multiple room names
        after the create_room command
        
        Usage:
            create_room <room_name>...
        """
        global amity
        multiple_rooms = arg["<room_name>"]
        for room in multiple_rooms:
            print('Room Name: '+room.upper())
            room_type = input("Enter a room type, either 'office' or 'living': ")
            valid = self.is_room_input_valid(room_type)
            if valid:
                amity.create_room({"room_name": room, "room_type": room_type})
            else:
                input("Please enter either 'office' or 'living': ")


    def is_room_input_valid(self, room_type):
        if room_type == "office" or room_type == "living":
            return True
        else:
            return False

    @docopt_cmd 
    def do_add_person(self, arg):
        """
        Create a person and assign them to a room in Amity. 

        Usage:
            add_person <person_name> [--accomodation=N]
        """
        global amity
        person = arg["<person_name>"]
        wants_accomodation = arg["--accomodation"]
        print('Name: '+person.upper())
        print('Wants Accomodation: '+wants_accomodation.upper())
        person_type = input("Enter a role, either 'staff' or 'fellow': ")
        valid = self.is_role_input_valid(person_type)
        if valid:
            amity.create_person({"person_name": person, "role": person_type, "wants_accomodation": wants_accomodation})
        else:
            input("Please enter either 'staff', 'fellow': ")
        #print(amity.get_list_of_people())
        #print(amity.get_list_of_allocated_staff())

    def is_role_input_valid(self, role):
        if role == 'staff' or role == 'fellow':
            return True
        else:
            return False

    @docopt_cmd
    def do_reallocate_person(self, arg):
        """
        Reallocate a person using their name and the new room name.new_room

        Usage:
            reallocate_person <person_name> 
        """
        global amity
        person_name = arg["<person_name>"]
        person = self.get_person(person_name)
        if person:
            print('Name: '+person.person.upper())
            new_room = input("Enter the name of the new room: ")
            amity.reallocate_person(person, new_room) 
        else: 
            print("This person does not exist!")

    def get_person(self, person_name):
        names = []
        for person in amity.all_people:
            names.append(person.person)
        if person_name not in names:
            return False
        else:
            for person in amity.all_people:
                if person.person == person_name:
                    return person
        





    @docopt_cmd
    def do_quit(self, arg):
        """
        Quits out of Interactive Mode.

        Usage:
            quit
        """

        #print(person_functions.add_people_to_db())
        #print(room_functions.add_rooms_to_db())
        print('Goodbye!')
        exit()

#if opt['--interactive']:
if __name__ == "__main__":
    try:
        intro()
        AmityInteractive().cmdloop()
    except KeyboardInterrupt:
        print('Application Exiting')