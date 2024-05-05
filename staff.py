from prettytable import PrettyTable

class Staff:
    """Small staff blueprint, who will be able to refil the machine"""
    def __init__(self) -> None:
        self.employer = "employer"
        self.employee = "employee"
        self.ingredients
    
    def refil_resources(self, resources_obj):
            """Refils the machine"""
            table = PrettyTable()

            resource_list = [ resources_obj.resources["water"], resources_obj.resources["milk"], resources_obj.resources["coffee"] ]
            table.add_column("Ingredients", ["water", "milk", "coffee"])
            table.add_column("Amount", resource_list)
            table.align = "l"
            
            print("Welcome lets refil the machine.")
            print(f"""Currently we have:\n{table}\n""")
            resources_obj.resources["water"] += int(input("Add Water. "))
            resources_obj.resources["milk"] += int(input("Add Milk. "))
            resources_obj.resources["coffee"] += int(input("Add Coffee. "))
            
            table.del_column("Amount")
            resource_list = [ resources_obj.resources["water"], resources_obj.resources["milk"], resources_obj.resources["coffee"] ]            
            table.add_column("Amount", resource_list)
            print(f"""\nThe new resources are:\n{table}\n""")