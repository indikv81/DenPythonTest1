import subprocess as sp
ip_1 = 10
ip_2 = 15
ip_3 = 11
ip_4 = 112
ip = str(ip_1) + "." + str(ip_2) + "." + str(ip_3) + "." + str(ip_4)
print(ip)
ip2 = "www.yandex.ru"
output = sp.check_output(["ping", "-n", "1", ip2]).decode('cp866', 'ignore')
print(output)

def ipcheck():
    status,result = sp.getstatusoutput("ping -n 1 " + str(ip))
    if status == 0:
        print("System " + str(ip) + " is UP !")
    else:
        print("System " + str(ip) + " is DOWN !")
    print(status)

ipcheck()