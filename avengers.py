with open('avengers.txt', 'r') as f:
    content = f.readlines()
    remove_duplicat_item = set(content)   #remove duplicat item using set()
    content = list(remove_duplicat_item)
    content.sort()
    a, b, c = [], [], []
    for i in content:
        
        # check that <alive> is in suffix
        if '<alive>' in i:
            remove_suffix = i.replace('<alive>', '')
            a.append(remove_suffix)

        # check that <dusted> is in suffix
        elif '<dusted>' in i:
            remove_suffix = i.replace('<dusted>', '')
            b.append(remove_suffix)

        # check that <died> is in suffix
        else:
            remove_suffix = i.replace('<died>', '')
            c.append(remove_suffix)


# file one alive.txt
    x1 = a[0].upper()
    y1 = a[-1].upper()
    a[0] = x1
    a[-1] = y1
    for j in a:
        with open('alive.txt', 'a') as f:
            f.write(j)

# file two dusted.txt
    x2 = b[0].upper()
    y2 = b[-1].upper()
    b[0] = x2
    b[-1] = y2
    for j in b:
        with open('dusted.txt', 'a') as f:
            f.write(j)

# file three died.txt
    x3 = c[0].upper()
    y3 = c[-1].upper()
    c[0] = x3
    c[-1] = y3
    for j in c:
        with open('died.txt', 'a') as f:
            f.write(j)