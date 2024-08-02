import json
import sys

parse_root = "targets"
dotnet_version_id = "net8.0"
arrow = "-->"
pipe =  "|"
spacer = ""
depth = 0

class item:
    def __init__(self, name, version, id):
        self.name = name
        self.version = version
        if(id == ""):
            self.id = name + '/' + version
        else:
            self.id = id
        
        self.children = [] 

def format_direct_dependency(name):
    space_position = name.find(" ")

    dependency_name = name[:space_position]
    dependency_version = name[space_position:]

    return [dependency_name,dependency_version]

def get_dependency_name_wo_version(name):
    space_position = name.find("/")

    new_name = name[:space_position]

    return new_name

def build_spacer(depth):
    gap = ""

    if(depth != 0):
        i=0
        while i < depth:
            gap = gap + " "
            i+=1

    return gap        

def print_tree(item):
    
    global depth
    gap = build_spacer(depth)
    depth = depth + 1

    name = item.name

    if(item.id == "root"):
        print(name)
    else:
        print(spacer + pipe)
        print(spacer + arrow + name + "("+ item.version +")")

    #print("d:" + str(depth))

    for child in item.children: 
        print_tree(child)

    depth = depth - 1

def find_item(item_id):
    print("item id: " + item_id)
    
    for library in all_libraries:

        demark = library.find("/")

        library_name = library[:demark]
                
        
        if(item_id == library_name):
            print("library name: " + library_name)
            if("dependencies" in library):
                print("has dependencies")
                return



input_file=sys.argv[1]
#libraries = []


with open(input_file, encoding='utf-8') as read_file:
    parsed_data = json.load(read_file)

project_file_dependencies_node = parsed_data["projectFileDependencyGroups"]
project_name = parsed_data["project"]["restore"]["projectName"]
project_version = parsed_data["project"]["version"]
all_libraries = parsed_data[parse_root][dotnet_version_id]

print("Processing file" + input_file + " for: " + project_name)

root = item(project_name, project_version,"root")
direct_dependencies = project_file_dependencies_node[dotnet_version_id]

for direct_dependency in direct_dependencies:
    formatted_direct_dependency = format_direct_dependency(direct_dependency)
    # print(formatted_direct_dependency)
    child = item(formatted_direct_dependency[0],formatted_direct_dependency[1],"")
    
    # check to see if library has any dependencies
    find_item(child.name)
    
    
    root.children.append(child)




print_tree(root)


# if (parse_root in parsed_data):
    # if (dotnet_version_id in parsed_data[parse_root]):
    #     libraries = parsed_data[parse_root][dotnet_version_id]
    #     for library in libraries.keys():
    #         print(library)
    #         root.children.append(item(library,"child"))

    #         if ("dependencies" in parsed_data[parse_root][dotnet_version_id][library]):
    #             for dependency in parsed_data[parse_root][dotnet_version_id][library]["dependencies"].keys():
    #                 print(spacer + pipe)
    #                 print(spacer + arrow + dependency) 

    #         print("")





# def build_tree():

#     range_limit = len(libraries)

#     for i in range(0,range_limit):
#         library = libraries[i]
#         root.children.append(library[0])


# def convert_package_name(package_name):
#     #"Microsoft.OpenApi": "1.2.3" 




# type: ignore #def print_tree():






