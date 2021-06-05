# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests


def get_file(file_path):
    try:
        file = open(file_path, "r")
        lines = (file.read()).split()
        file.close()
        return lines
    except:
        print("Invalid filepath")
        return ""


def get_dir_exists(base, dir):
    try:
        if requests.head(base + "/" + dir).status_code == 200:
            return True

        return False

    except:
        return False


def get_all_dir(dictionary, website, get_sub_dir, count_deep):
    output = []

    if count_deep > 3:
        return output

    if dictionary != "":
        for line in dictionary:
            if get_dir_exists(website, line):
                print(website + "/" + line)
                output.append(line)

                if get_sub_dir == True:
                    output.append(get_all_dir(dictionary, website+"/"+line, True, count_deep+1))
    else:
        print("Empty Dictionary")

    return output


file_path_user = input("Small(s), Medium(m) or Big(b): ")
website_url = input("Enter a website URL (include https://): ")
sub_dir = input("Search subdirectories (y/n)")

file_path = "directory-list-2.3-big.txt"
if file_path_user == "s":
    file_path = "directory-list-2.3-small.txt"
if file_path_user == "m":
    file_path = "directory-list-2.3-medium.txt"
if file_path_user == "test":
    file_path = "directory-test.txt"


search_sub_dir = False
if sub_dir == "y":
    search_sub_dir = True


list_dir = get_all_dir(get_file(file_path), website_url, search_sub_dir, 0)
#for i in list_dir:
#    print(i)



print("Finished!")
