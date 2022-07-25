import hcl

with open('../main.tf','r') as fp:
    obj = hcl.load(fp)

    print(obj)