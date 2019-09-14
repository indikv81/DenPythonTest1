import subprocess as sp

def ipcheck(fnip):
    print("Тест: " + fnip)
    status, result = sp.getstatusoutput("ping -n 1 " + str(fnip))
    if status == 0:
        print("System " + str(fnip) + " is UP !")
    else:
        print("System " + str(fnip) + " is DOWN !")
    print(status)

ip_1 = 192
ip_2 = 168
ip_3 = 1
ip_4 = 1
ip = str(ip_1) + "." + str(ip_2) + "." + str(ip_3) + "." + str(ip_4)
print(ip)
output = sp.check_output(["ping", "-n", "1", ip]).decode('cp866', 'ignore')
print(output)
ipcheck(ip)

ip2 = "www.yandex.ru"
output = sp.check_output(["ping", "-n", "1", ip2]).decode('cp866', 'ignore')
print(ip2)
print(output)
ipcheck(ip2)