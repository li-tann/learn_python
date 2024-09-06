dict_has_id = []
dict_nul_id = []

with open('dongle_id_map.txt','r') as f:
    strlsit = f.readlines()
    for s in strlsit:
        # print(s)
        sslist = s.split()
        # print(sslist)
        if sslist[1] != 'null':
            dict_has_id.append("\"{}\":{}".format(sslist[1], sslist[0]))
        else:
            dict_nul_id.append(sslist[0])


print("dict_has_id:\n", dict_has_id)
print("dict_nul_id:\n", dict_nul_id)


with open('dict_has_id.txt','w') as f:
    f.write("{\n")
    for i in dict_has_id:
        f.write('{},\n'.format(i))
    f.write("}\n")

with open('dict_nul_id.txt','w') as f:
    f.write("{\n")
    for i in dict_nul_id:
        f.write('{},\n'.format(i))
    f.write("}\n")