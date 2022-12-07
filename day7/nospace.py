import fileinput


class Folder:
    def __init__(self, name, parent):
        self.name = name
        self.size = 0
        self.folders = []
        self.parent = parent

    def size_including_subfolders(self):
        sum = self.size
        for folder in self.folders:
            sum += folder.size_including_subfolders()
        return sum

    def get_folder_list(self):
        sizes = []
        sizes.append(self.size_including_subfolders())
        for folder in self.folders:
            sizes.extend(folder.get_folder_list())
        return sizes

    def print_tree(self, level=0):
        print("  " * level, self.name, self.size)
        for folder in self.folders:
            folder.print_tree(level + 1)

    def __str__(self):
        return "" + self.name + " size: " + str(self.size)


# vi ser bort fra dir-kommandoen. vi oppretter heller folders med cd.
# ls() gir kun ut størrelsen på filene i den aktuelle katalogen
def ls(ls_response):
    sum = 0
    for response in ls_response:
        subresponse = response.split()[0]
        if subresponse != "dir":
            sum += int(subresponse)
    return sum


def solve():
    commands = []
    for line in fileinput.input():
        commands.append(line.strip())
    root = Folder("/", None)
    current_folder = root
    pos = 1
    while pos < len(commands):
        if commands[pos].startswith("$ cd"):
            subcommand = commands[pos].split()[2]
            if subcommand == "..":
                current_folder = current_folder.parent
            else:
                new_folder = Folder(subcommand, current_folder)
                current_folder.folders.append(new_folder)
                current_folder = new_folder
        elif commands[pos] == "$ ls":
            ls_response = []
            pos += 1
            while (pos < len(commands)) and (commands[pos][0] != "$"):
                ls_response.append(commands[pos])
                pos += 1
            size = ls(ls_response)
            current_folder.size = size
            pos -= 1
        else:
            print("should not occur, bug or error in input")
            return
        pos += 1
    total = 0
    for elem in root.get_folder_list():
        # check if the element is less than n
        if elem < 100000:
            # if it is, add it to the total
            total += elem
    print("part one:", total)

    size_on_disk = root.size_including_subfolders()
    size_to_be_freed = 30000000 - (70000000 - size_on_disk)
    smallest_folder = 70000000
    for folder_size in root.get_folder_list():
        if folder_size < smallest_folder and folder_size > size_to_be_freed:
            smallest_folder = folder_size
    print("part two:", smallest_folder)


solve()
