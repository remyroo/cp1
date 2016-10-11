"""
Usage:
    amity create_room (Living|Office) <room_name>...
    amity add_person <first_name> <last_name> (Fellow|Staff) [<wants_space>]
    amity reallocate_person <employee_id> <new_room_name>
    amity load_people <filename>
    amity print_allocations [--o=filename.txt]
    amity print_unallocated [--o=filename.txt]
    amity print_room <room_name>
    amity save_state [--db=sqlite_database]
    amity load_state <sqlite_database>
    amity (-i | --interactive)
Options:
    -h --help     Show this screen.
    -i --interactive  Interactive Mode
    -v --version
"""

from docopt import docopt
from models.amity import amity

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


class AmityInteractive(cmd.Cmd):

    #cprint(figlet_format('AMITY', font='univers'), 'cyan', attrs=['bold'])

    def introduction():
        print (border)
        print (spacer)
        print ("WELCOME TO AMITY SPACE ALLOCATION!".center(70))
        print ("Allocate rooms to people at random".center(70))
        print (spacer)
        print ("ROOM ALLOCATION COMMANDS:".center(70))
        print (spacer)
        # print "1. create_room (Living|Office) <room_name>...".center(70)
        # print "2. add_person " \
        #     "< first_name> <last_name> (Fellow|Staff) " \
        #     "[<wants_space>]".center(70)
        # print "3. reallocate_person <employee_id> <new_room_name>".center(70)
        # print "4. load_people <filename>".center(70)
        # print "5. print_allocations [--o=filename.txt]".center(70)
        # print "6. print_unallocated [--o=filename.txt]".center(70)
        # print "7. print_room <room_name>".center(70)
        # print "8. save_state [--db=sqlite_database]".center(70)
        # print "9. load_state <sqlite_database>".center(70)
        # print spacer
        # print "OTHER COMMANDS:".center(70)
        # print spacer
        # print "1. help".center(70)
        # print "2. quit".center(70)
        # print spacer
        # print border

    intro = introduction()
    prompt = "(amity)"
    file = None

    @docopt_cmd
    def create_room(self, arg):
        """
        Create a room in Amity. A room can either be an office or living space.
        Create as many rooms as possible by specifying multiple room names
        after the create_room command
        
        Usage:
            create_room <room_name>...
        """

        amity.create_room(args)

    def do_quit(self, arg):
        """
        Quits out of Interactive Mode.
        """

        print(person_functions.add_people_to_db())
        print(room_functions.add_rooms_to_db())
        print('Good Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    AmityInteractive().cmdloop()