from subprocess import PIPE, Popen

command = "adb devices"
with Popen(command, stdout=PIPE, stderr=None, shell=True) as process:
    output = process.communicate()[0].decode("utf-8")
    lst = output.split('\n')
    op = lst[1]
    if len(op) > 10:
        command = "adb shell ifconfig"
        with Popen(command, stdout=PIPE, stderr=None, shell=True) as process:
            output = process.communicate()[0].decode("utf-8")
            lst = output.split("wlan0")[1].split("inet addr")
            if len(lst) > 1:
                ip = lst[1][1:14]
                print("device ip =", ip)
                command = "adb tcpip 555"
                with Popen(command, stdout=PIPE, stderr=None, shell=True) as process:
                    output = process.communicate()[0].decode("utf-8")
                    command = "adb connect "+ip+":5555"
                    with Popen(command, stdout=PIPE, stderr=None, shell=True) as process:
                        output = process.communicate()[0].decode("utf-8")
                        print(output)
            else:
                print("device not connected to internet/lan... quitting ")
            # print(lst[1][1:14])

    else:
        print("no device connected ...\nquiting.....")
