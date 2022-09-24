NOS = [
    ['z', 'e', 'r', 'o'],
    ['o', 'n', 'e'],
    ['t', 'w', 'o'],
    ['t', 'h', 'r', 'e', 'e'],
    ['f', 'o', 'u', 'r'],
    ['f', 'i', 'v', 'e'],
    ['s', 'i', 'x'],
    ['s', 'e', 'v', 'e', 'n'],
    ['e', 'i', 'g', 'h', 't'],
    ['n', 'i', 'n', 'e']
]

inp = input()

s = []

for i in inp:
    s.append(i)

def find_no(s, no):
    print(type(s))
    str_copy = s.copy()

    n = -1

    ele_present = True

    while ele_present:
        for i in no:
            if i in str_copy:
                s.remove(i)
            else:
                ele_present = False
                break
        n +=1
        s = str_copy
    return str, n

output = ""

for i in NOS:
    s, n = find_no(s, i)
    output = output + str(i)*n

print(output)
