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


def find_string(inp):
    s = []

    for i in inp:
        s.append(i)

    def find_no(s, no):

        n = -1

        scp = s.copy()

        ele_present = True

        while ele_present:
            for i in no:
                if i in scp:
                    scp.remove(i)
                else:
                    ele_present = False
                    break
            if ele_present:
                s = scp
            n +=1

        # print(s)
        return scp, n

    output = ""

    for i in range(len(NOS)):
        t, n = find_no(s, NOS[i])
        output = output + str(i)*n

    return output

def smallest(lst):
    if int(''.join(lst)) == 0:
        return "0"

    for i,n in enumerate(lst):
        if n != '0':
            tmp = lst.pop(i)
            break
    return str(tmp) + ''.join(lst)




lst = []
test_case = int(input())
for i in range(test_case):
    inp = input()
    lst.append(smallest(list(find_string(inp))))


for i in lst:
    print(i)


