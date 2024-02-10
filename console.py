#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """CLI for HBNB project"""
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing when the user enters an empty line."""
        pass

    def do_create(self, args):
        """Creates a new instance of the specified class.
        Usage: create <class>"""
        if not args:
            print("** class name missing **")
            return
        class_name = args.split()[0]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        new_instance = eval(f"{class_name}()")
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """
        Prints the string representation
        of an instance based on the class name and id.
        """
        largs = args.split()

        if not largs:
            print("** class name missing **")
            return

        class_name = largs[0]

        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        if len(largs) < 2:
            print("** instance id missing **")
            return

        instance_id = largs[1]
        k = "{}.{}".format(class_name, instance_id)

        if k not in storage.all():
            print("** no instance found **")
            return

        instance = storage.all()[k]
        print(instance)


    def do_all(self, args):
        """Prints all string representations of instances
        based on the class name.
        Usage: all <class_name> or all"""
        if args:
            class_name = args.split()[0]

            if class_name not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return

            instances = storage.all().values()

            filtered_instances = [
                str(instance) for instance in instances
                if instance.__class__.__name__ == class_name
            ]

            print(filtered_instances)

        else:
            instances = storage.all().values()
            print([str(instance) for instance in instances])

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        """
        largs = args.split(" ")

        if len(largs) == 1:
            print("** class name missing **")
            return
        class_name = largs[0]

        if class_name not in models.__dict__:
            print("** class doesn't exist **")
            return

        if len(largs) == 2:
            print("** instance id missing **")
            return
        instance_id = largs[1]

        key = "{}.{}".format(class_name, instance_id)
        if key not in self.__objects:
            print("** no instance found **")
            return

        if len(largs) == 3:
            print("** attribute name missing **")
            return
        attribute_name = largs[2]

        if len(largs) == 4:
            print("** value missing **")
            return
        attribute_value_str = largs[3]

        if attribute_value_str[0] == '"' and attribute_value_str[-1] == '"':
            attribute_value_str = attribute_value_str[1:-1]

        cls = models.__dict__[class_name]
        attribute_type = type(getattr(cls(), attribute_name, None))

        try:
            attribute_value = attribute_type(attribute_value_str)
        except ValueError:
            print("** value missing **")
            return

        instance = self.__objects[key]
        setattr(instance, attribute_name, attribute_value)

        self.save()



    def do_destroy(self, args):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file).
        Usage: destroy <class_name> <id>"""
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        class_name = args_list[0]

        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        instance_id = args_list[1]
        instances = storage.all()
        instance_key = "{}.{}".format(class_name, instance_id)

        if instance_key not in instances:
            print("** no instance found **")
            return

        del instances[instance_key]

        storage.save()


    def do_quit(self, args):
        """Exit the CLI"""
        return True

    def do_EOF(self, args):
        """Exit the CLI on Ctrl+D"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
