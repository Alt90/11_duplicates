import sys
import os


def find_duplicates(search_dir, all_file_in_dir={}):
    duplicates = []
    for file_path, search_sub_dir, search_files in os.walk(search_dir):
        for search_file in search_files:
            full_file_name = u'%s/%s' % (file_path, search_file)
            file_key = u'%s-%s' % (search_file,
                                   os.path.getsize(full_file_name))
            file_path_in_dict = all_file_in_dir.get(file_key, False)
            if file_path_in_dict:
                duplicates.append([file_path_in_dict, full_file_name])
            else:
                all_file_in_dir[file_key] = full_file_name
    return duplicates


def print_duplicates(duplicates):
    for duplicate in duplicates:
        print(u'%s - %s' % (duplicate[0], duplicate[1]))


if __name__ == '__main__':
    if (len(sys.argv) < 2):
        search_dir = '../'
    else:
        search_dir = sys.argv[1]
    duplicates = find_duplicates(search_dir)
    print_duplicates(duplicates)
