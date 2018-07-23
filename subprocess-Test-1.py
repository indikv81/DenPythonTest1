import subprocess
output = subprocess.check_output(["pip", "list"]).decode('UTF-8','ignore')

output = output.split()
output = output[4:]
mod_name = output[::2]
mod_version = output[1::2]
modules = dict(zip(mod_name, mod_version))
for x in modules:
    print("Модуль: '" + x + "' - версия: " + modules[x])