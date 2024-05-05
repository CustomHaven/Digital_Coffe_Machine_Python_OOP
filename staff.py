from prettytable import PrettyTable


class Staff:
    """Small staff blueprint, who will be able to refil the machine"""
    def __init__(self) -> None:
        self.employer = "employer"
        self.employee = "employee"
    
    def refil_resources(self, resources_obj):
            table = PrettyTable()
            table.align = "l"
            resource_list = [ resources_obj.resources['water'], resources_obj.resources['milk'], resources_obj.resources['coffee'] ]
            table.add_column("Ingredients", ["water", "milk", "coffee"])
            table.add_column("Amount", resource_list)
            # for key, val in resources_obj.items():
            #      print(key, val)
            print("Welcome lets refil the machine.")
            print(f"""\nCurrently we have:\n{table}""")
            resources_obj.resources["water"] += int(input("Add Water. "))
            resources_obj.resources["milk"] += int(input("Add Milk. "))
            resources_obj.resources["coffee"] += int(input("Add Coffee. "))
            # table.add_column("Amount", resource_list)
            table.del_column("Amount")
            resource_list = [ resources_obj.resources['water'], resources_obj.resources['milk'], resources_obj.resources['coffee'] ]
            

            table.add_column("Amount", resource_list)
            print(f"""\nThe new resources are:\n{table}""")