import yaml


def read_yaml(filename):
    path = "../datas/" + filename
    with open(path, "rb") as f:
        data = yaml.safe_load(f)
    return data


arrs = []
for i in read_yaml("login.yaml").values():
    arrs.append(i)
    print(arrs)
