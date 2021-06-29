import yaml


def read_yaml(filename):
    path = "../datas/" + filename
    with open(path, "rb") as f:
        data = yaml.safe_load(f)
    return data


# 登录
def get_login_data():
    arrs = []
    for i in read_yaml("login.yaml").values():
        arrs.append((i['username'], i['pwd'], i['expect'], i['success'], i['title']))
    return arrs


print(get_login_data())
