import subprocess
output = subprocess.check_output(["pip", "list"]).decode('UTF-8','ignore')

output = output.split()
output = output[4:]
mod_name = output[::2]
mod_version = output[1::2]
modules = dict(zip(mod_name, mod_version))
for x in modules:
    print("Модуль: '" + x + "' - версия: " + modules[x])

def outputm(mod_name):
    output_info = subprocess.check_output(["pip", "show", mod_name]).decode('UTF-8','ignore')
    output_info = output_info.splitlines()
    mod_param_key = list(map(lambda x: x[:x.index(':')], output_info))
    mod_param_value = list(map(lambda x: x[x.index(':') + 2:], output_info))
    return dict(zip(mod_param_key, mod_param_value))

dict_info = {}
for x in mod_name:
    dict_info.update({x : outputm(x)})
    print(dict_info[x]['Name'] + ' ' + dict_info[x]['Version'] + ' (' + dict_info[x]['Summary'] + ') ' + dict_info[x]['Home-page'])
#print(dict_info)
