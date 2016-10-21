"""
Usage:
    create_room (Living|Office) <room_name>...
    add_person <person_name> (Fellow|Staff) [--accomodation=no]
    reallocate_person <person_name> <new_room_name>
    load_people <filename>
    print_allocations [--o=filename]
    print_unallocated [--o=filename]
    print_room <room_name>
    save_state [--db=sqalchemy_database]
    load_state <sqalchemy_database>
    quit
    
Options:
    --h               Show this screen.
    --o               Specify filename
    --db              Name of SQAlchemy database
    --accommodation   If person needs accommodation [default='no']
"""

import cmd
from docopt import docopt, DocoptExit
from models.db_actions import Database, amity

database = Database()

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
    print ("WELCOME TO AMITY SPACE ALLOCATION!".center(70))
    print ("Allocate rooms to staff and fellows in Amity".center(70))
    print ("-> help".center(70))
    print ("-> quit".center(70))


class AmityInteractive(cmd.Cmd):
    prompt = 'Start>>>  '

    @docopt_cmd
    def do_create_room(self, arg):
        """
        Creates a room in Amity. A room can either be an office or living space.
        Create as many rooms as possible by specifying multiple room names
        after the create_room command.
        
        Usage:
            create_room <room_name>...
        """
        global amity
        multiple_rooms = arg["<room_name>"]
        for room in multiple_rooms:
            print("Room Name: "+room.upper())
            room_type = input("Enter a room type, either 'office' or 'living': ")
            valid = self.is_room_input_valid(room_type)
            if valid:
                amity.create_room({"room_name": room, "room_type": room_type})
            else:
                print ("\n Please try again. Remember to enter either 'office' or 'living'. \n")


    def is_room_input_valid(self, room_type):
        if room_type == "office" or room_type == "living":
            return True
        else:
            return False

    @docopt_cmd 
    def do_add_person(self, arg):
        """
        Creates a person and assign them to a room in Amity. 

        Usage:
            add_person <person_name> [--accomodation=no]
        """
        global amity
        person = arg["<person_name>"]
        wants_accomodation = arg["--accomodation"]
        print("Name: "+person.upper())
        person_type = input("Enter a role, either 'staff' or 'fellow': ")
        valid = self.is_role_input_valid(person_type)
        if wants_accomodation == "yes" or wants_accomodation == "no":
            print("Wants Accomodation: "+wants_accomodation)
        if valid:
            amity.create_person({"person_name": person, "role": person_type, "wants_accomodation": wants_accomodation})
        else:
            print ("\n Please try again. Remember to enter either 'staff' or 'fellow'. \n")

    def is_role_input_valid(self, role):
        if role == "staff" or role == "fellow":
            return True
        else:
            return False

    @docopt_cmd
    def do_reallocate_person(self, arg):
        """
        Reallocates a person from their current room to another room.

        Usage:
            reallocate_person <person_name> 
        """
        global amity
        person_name = arg["<person_name>"]
        person = self.get_person(person_name)
        if person:
            print("Name: "+person.person.upper())
            new_room = input("Enter the name of the new room: ")
            amity.reallocate_person(person, new_room) 
        else: 
            print("This person does not exist!")

    def get_person(self, person_name):
        '''
        This is a helper function that verifies the person entered 
        exists in the list of all people. 
        '''
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
    def do_load_people(self, arg):
        '''
        Add people to rooms from a txt file.

        Usage:
            load_people <filename>
        '''
        global amity
        filename = arg["<filename>"]
        amity.load_people_from_file(filename)

    @docopt_cmd
    def do_print_allocations(self, arg):
        '''
        Print the room and people allocations.

        Usage: 
            print_allocations [--o=filename]
        '''
        global amity
        filename = arg["--o"]
        if filename:
            amity.write_allocated_to_file(filename)
        else:
            amity.write_allocated_to_terminal()
        
    @docopt_cmd
    def do_print_unallocated(self, arg):
        '''
        Print the people who have not been allocated a room.

        Usage: 
            print_unallocated [--o=filename]
        '''
        global amity
        filename = arg["--o"]
        if filename:
            amity.write_unallocated_to_file(filename)
        else:
            amity.write_unallocated_to_terminal()

    @docopt_cmd
    def do_print_room(self, arg):
        '''
        Print the people allocated to a specified room.

        Usage:
            print_room <room_name>
        '''
        global amity
        room_name = arg["<room_name>"]
        amity.print_room(room_name)

    @docopt_cmd
    def do_save_state(self, arg):
        '''
        Save all the data in the app to a SQAlchemy database. 
        Specifying the --db parameter explicitly stores the data
        in the database specified.

        Usage:
            save_state [--db=sqalchemy_database]
        '''
        global amity
        db_name = arg["--db"]
        if db_name:
            database.save_state(db_name)
            text = "The application data has been saved to "+db_name.upper()
        else:
            database.save_state("amity.db")
            text = "The application data has been saved to AMITY.DB"
        print (text)
       
    
    @docopt_cmd
    def do_load_state(self, arg):
        '''
        Loads data from a specified database into the application.

        Usage:
            load_state <sqalchemy_database>
        '''
        global amity
        db_name = arg["<sqalchemy_database>"]
        database.load_state(db_name)
        print ("The application data has been loaded from "+db_name.upper())

    @docopt_cmd
    def do_quit(self, arg):
        """
        Quits out of Interactive Mode.

        Usage:
            quit
        """

        print("Goodbye!")
        exit()


if __name__ == "__main__":
    try:
        intro()
        AmityInteractive().cmdloop()
    except KeyboardInterrupt:
        print("Application Exiting")