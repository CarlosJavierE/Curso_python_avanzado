# [1, 1, 2, 2, 4] -> [1, 2, 4]

def remove_duplicates(some_list):
    without_duplicates = []
    for elememnt in some_list:
        if elememnt not in without_duplicates:
            without_duplicates.append(elememnt)
    return without_duplicates

def remove_with_sets(lista):
    return list(set(lista))

def run():
    random_list = [1, 1, 2, 2, 4, 4, 4, 5, 5, 7, 7, 7, 1, 1, 1, 3, 3]
    print(remove_duplicates(random_list))

    print(remove_with_sets(random_list))

if __name__ == '__main__':
    run()