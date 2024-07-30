import json
import sys

class item:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.children = [] 

input_file=sys.argv[1]
#libraries = []

parse_root = "targets"
dotnet_version_id = "net8.0"
arrow = "-->"
pipe =  "|"


with open(input_file, encoding='utf-8') as read_file:
    parsed_data = json.load(read_file)

project_name = parsed_data["project"]["restore"]["projectName"]

print("Processing file" + input_file + " for: " + project_name)

root = item(project_name, "root")

if (parse_root in parsed_data):
    if (dotnet_version_id in parsed_data[parse_root]):
        libraries = parsed_data[parse_root][dotnet_version_id]
        for library in libraries.keys():
            print("library:" + library)
            root.children.append(item(library,"child"))

            for dependency in parsed_data[parse_root][dotnet_version_id][library]["dependencies"].keys():
                print(pipe)
                print(arrow + dependency) 

       

def build_tree():

    range_limit = len(libraries)

    for i in range(0,range_limit):
        library = libraries[i]
        root.children.append(library[0])


#def print_tree():







