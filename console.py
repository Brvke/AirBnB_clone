#!/usr/bin/python3
import cmd
import sys
import re
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classdicts = {"BaseModel":BaseModel,"User": User, "Amenity": Amenity,
             "Place": Place, "Review": Review, "City": City, "State": State}
    classkeys = classdicts.keys()
    
    def do_create(self, args):
        """Creates a new instance of BaseModel,
        saves it as json file and prints the id"""
        if args:
            if args in HBNBCommand.classkeys:
                newobj = HBNBCommand.classdicts[args]()
                storage.save()
                print(newobj.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        return

   
    def do_show(self, command):
        """ print the string representation of an instance
        basedon the class name and id"""
        args = command.split()

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]
        search_key = f"{class_name}.{instance_id}"

        if class_name not in self.classkeys:
            print("** class does't exist **")
        else:
            obj_dict = storage.all()
            obj = obj_dict.get(search_key)
            if obj:
                print(obj)
            else:
                print("** no instance found **")
    
    def do_destroy(self, command):
        """ deletes an instance based on the class name 
        and id and save th change into json file
        """
        args = command.split()  # splits command line into list of arguments
        objdict = storage.all()

        if len(args) == 2:
            if args[0] not in HBNBCommand.classkeys:
                print("** class doesn't exist **")
            else:
                """
                    when user passes <class> <class.id> merge it into
                    a string with the format <class>.<class.id>
                    and then search for it in FileStorage.__object dict if
                    found delete it and save the new FileStorage.__object dict
                """
                objdict = storage.all()
                searchkey = f'{args[0]}.{args[1]}'
                if searchkey in objdict.keys():
                    del objdict[searchkey]
                    storage.save()
                else:
                    print("** no instance found **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            print("** class name missing **")
    def do_all(self, command):
        """ Prints all string representation of all instances
            based or not on the class name. Ex: $ all BaseModel or $ all"""

        args = command.split()
        object_dict = storage.all()

        if len(args) == 1:
            if args[0] in HBNBCommand.classkeys:
                for obj in object_dict.keys():
                    if args[0] == object_dict[obj].__class__.__name__:
                        print(object_dict[obj])
            else:
                print("** class doesn't exist **")
        elif len(args) == 0:
            for obj in object_dict.keys():
                print(object_dict[obj])

    def do_count(self, command):
        """return the number of instances belonging
        toa specific class"""
        args = command.split()

        obj_dict = self.storage.all()
        count = 0

        if len(args) == 1:
            class_name = args[0]
            if class_name in self.classkeys:
                count = sum(1 for obj in obj_dict.values()
                        if isinstance(obj, sel.classkeys[class_name]))
            else:
                print("** class doesn't exist **")
                return

        print(count)
    
    def do_update(self, commands):
        """Updates an instance based on the class name and id by
            adding or updating attribute (save the change into the JSON file).
            Ex: $ update BaseModel 1234-1234-1234 email 'aibnb@mail.com'
        """
        args = commands.split()
        if len(args) == 4:
            storedict = storage.all()  # stores all object in Storedict
            storekeys = storedict.keys()  # stores key  for sotrekeys
            key = f'{args[0]}.{args[1]}'
            if args[0] in HBNBCommand.classdicts.keys():
                if key in storekeys:
                    # if the key is in storekeys updates corsponding instance
                    value = re.findall(r'(?<=")(\S+|\s+)(?=")', args[3])
                # using regex to remove " from beginig and end of attribute
                    if value:
                        setattr(storedict[key], args[2], value[0])
                    else:
                        setattr(storedict[key], args[2], args[3])
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(args) == 3:
            print("** value missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 0:
            print("** class name missing **")

    def emptyline(self):
        """ If this method is overriddes, the built in emptyline
            function which repeats the last nonempty command entered.
        """
        return
    
    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program
        """
        return True

    def precmd(self, line):
        """parses input from the command line to handle
        <classname>.<cmd>(variable) cases"""
        args = line.split()
        if args:
            new_line = self.Regex(args)
            return new_line if new_line else line
        return line

    def Regex(self, line):
        """Parses <class name>.all() type commands to 
        the appropriate version line: list"""

        pattern = r'(?<=\S)\.(?=\S)'
        result = re.split(pattern, line[0])

        if result == [line[0]]:
            return None

        new_list = re.split(r'\(\)', result[1])
        if new_list != [result[1]]:
            return f'{new_list[0]} {result[0]}'

        id = re.findall(r'(?<=\(").+(?="\))', result[1])
        cmd = re.findall(r'^\w+', result[1])
        if id:
            return f'{cmd[0]} {result[0]} {id[0]}'
                
if __name__ == '__main__':
    HBNBCommand().cmdloop()

