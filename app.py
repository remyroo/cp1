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
        for room in arg["<room_name>"]:
            print ("Room Name: "+room.upper())
            room_type = input("Enter a room type, either 'office' or 'living': ")
            if room_type in ["office", "living"]:
                amity.create_room({"room_name": room, "room_type": room_type})
            else: print ("\n Please try again. Remember to enter either 'office' or 'living'. \n")

    @docopt_cmd 
    def do_add_person(self, arg):
        """
        Creates a person and assign them to a room in Amity. 

        Usage:
            add_person <first_name> <last_name> [--accomodation=no]
        """
        person = arg["<first_name>"] + " " + arg["<last_name>"]
        wants_accomodation = arg["--accomodation"]
        print ("Name: "+person.upper())
        person_type = input("Enter a role, either 'staff' or 'fellow': ")
        if wants_accomodation in ["yes", "Y", "no"]: print ("Wants Accomodation: "+wants_accomodation)
        if person_type in ["staff", "fellow"]: amity.create_person(
            {"person_name": person, "role": person_type, "wants_accomodation": wants_accomodation})
        else: print ("\n Please try again. Remember to enter either 'staff' or 'fellow'. \n")

    @docopt_cmd
    def do_reallocate_person(self, arg):
        """
        Reallocates a person from their current room to another room.

        Usage:
            reallocate_person <first_name> <last_name> 
        """
        person_name = arg["<first_name>"] + " " + arg["<last_name>"]
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
        names = [person.person for person in amity.all_people]
        if person_name not in names: return False
        else: 
            person = [person for person in amity.all_people if person.person == person_name][0]
            return person

    @docopt_cmd
    def do_load_people(self, arg):
        '''
        Add people to rooms from a txt file.

        Usage:
            load_people <filename>
        '''
        amity.load_people_from_file(arg["<filename>"])

    @docopt_cmd
    def do_print_allocations(self, arg):
        '''
        Print the room and people allocations.

        Usage: 
            print_allocations [--o=filename]
        '''
        if arg["--o"]: amity.write_allocated_to_file(arg["--o"])
        else: amity.write_allocated_to_terminal()
        
    @docopt_cmd
    def do_print_unallocated(self, arg):
        '''
        Print the people who have not been allocated a room.

        Usage: 
            print_unallocated [--o=filename]
        '''
        if arg["--o"]: amity.write_unallocated_to_file(arg["--o"])
        else: amity.write_unallocated_to_terminal()

    @docopt_cmd
    def do_print_room(self, arg):
        '''
        Print the people allocated to a specified room.

        Usage:
            print_room <room_name>
        '''
        amity.print_room(arg["<room_name>"])

    @docopt_cmd
    def do_save_state(self, arg):
        '''
        Save all the data in the app to a SQAlchemy database. 
        Specifying the --db parameter explicitly stores the data
        in the database specified.

        Usage:
            save_state [--db=sqalchemy_database]
        '''
        db_name = arg['--db'] or 'amity.db'
        database.save_state(db_name)
        print ("The application data has been saved to "+db_name.upper()+"\n")

    @docopt_cmd
    def do_load_state(self, arg):
        '''
        Loads data from a specified database into the application.

        Usage:
            load_state <sqalchemy_database>
        '''
        database.load_state(arg["<sqalchemy_database>"])
        print ("\n The application data has been loaded from "+arg["<sqalchemy_database>"].upper()+"\n")

    @docopt_cmd
    def do_quit(self, arg):
        """
        Quits out of Interactive Mode.

        Usage:
            quit
        """
        print ("Goodbye!")
        exit()


if __name__ == "__main__":
    try:
        intro()
        AmityInteractive().cmdloop()
    except KeyboardInterrupt:
        print ("\n Application Exiting \n")

