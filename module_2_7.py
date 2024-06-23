def print_params(a = 12, b = 'String', c = True):
    print(a, b, c)

print_params()

print_params('str', 12)

print_params(b = 25)

print_params(c = [1, 2, 3])

values_list = [False, 12.4, 'Alex']
values_dict = {'a' : 45, 'b' : True, 'c' : 'Max'}
print_params(*values_list)
print_params(**values_dict)

values_list2 = ['Word', 15]
print_params(*values_list2, 42)