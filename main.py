import sys

def read_file(file_name: str) -> list:
    if len(sys.argv) > 1:
        file_name = f"./txts/arquivo{sys.argv[1]}.txt"
    with open(file_name, "r") as file:
        n_people = int(file.readline())
        line = []
        for _ in range(n_people):
            line.append(list(file.readline().strip()))
    return line

def print_dict(dict_people: dict):
    for key, value in dict_people.items():
        print(f"{key}: {value}")

def check_if_is_valid(dict_people: dict):
    for _ , value in dict_people.items(): 
        for j in value:
            if value != dict_people[j]:
                return False
    return True

def count_and_print(dict_people: dict, pretty_print: bool):
    merged = {}
    #ATUALMENTE DICT_PEOPLE ESTÁ NO FORMATO {1: [1, 3, 2: [2, 4], 3: [1, 3], 4: [2, 4], 7: [7]}
    for key, value in dict_people.items():
        value_tuple = tuple(value)
        if value_tuple in merged:
            merged[value_tuple].append(key)
        else:
            merged[value_tuple] = [key]
    #AGORA ESTÁ NO FORMATO {(1, 3): [1, 3], (2, 4): [2, 4], (7): [7]}
    if pretty_print:
        print(f"{len(merged)} FAMÍLIAS")
        for i, value in enumerate(merged.values()):
            print(f"FAMÍLIA {i+1}: {len(value)} {'PESSOAS' if len(value) > 1 else 'PESSOA'}")
    else:
        print(len(merged))
        for i, value in enumerate(merged.values()):
            print(len(value), end=" ")


def solve(pretty_print = False) -> None:
    list_people = read_file("./txts/arquivo1.txt")
    flag_break = False
    families = {}
    result = ""
    #MONTANDO O DICIONÁRIO COM AS FAMÍLIAS NO FORMATO KEY (Pessoa): [VALUES] (Lista de pessoas da família, incluindo ela própria)
    for i in range(len(list_people)):
        families[i+1] = []
        if flag_break:
            break
        for j in range(len(list_people)):
            if i == j and list_people[i][j] != 'V': 
                result = "INFELIZMENTE OS C(K)AIOS ESTAVAM BÊBADOS"
                flag_break = True
                break;
            if list_people[i][j] != list_people[j][i]:
                result = "INFELIZMENTE OS C(K)AIOS ESTAVAM BÊBADOS"
                flag_break = True
                break
            if list_people[i][j] == 'V':
                families[i+1].append((j+1))
    # print_dict(familias)
    if flag_break:
        print(result)
        return
    if not check_if_is_valid(families):
        result = "INFELIZMENTE OS C(K)AIOS ESTAVAM BÊBADOS"
        print(result)
    else:
        count_and_print(families, pretty_print)

solve(True)
# print(ler_arquivo("./txts/arquivo2.txt"))
