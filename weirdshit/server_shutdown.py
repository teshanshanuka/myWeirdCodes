#This will use ssh to access the server and restart/shut it down
import sys, subprocess

HOST =  "Administrator@192.168.0.100"
SHUTDOWN_COMMAND = "shutdown /s"
RESTART_COMMAND = "shutdown /r"

input("\nIf you don't know what you are doing EXIT NOW!\n\nPress enter to continue")

print("Press r to restart or s to shutdown the server...")
what = input("Press any other key to do nothing and exit\n")

if what == 'r':
    print("Restarting...")
    ssh = subprocess.Popen(["ssh", "%s" % HOST, RESTART_COMMAND], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
elif what == 's':
    print("Shutting Down...")
    ssh = subprocess.Popen(["ssh", "%s" % HOST, SHUTDOWN_COMMAND], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
else:
    print("Exiting")
    sys.exit()

result = ssh.stdout.readlines()
if result == []:
    error = ssh.stderr.readlines()
    print("ERROR: %s" % error, file=sys.stderr)
else:
    print(result)
input("Press enter...")
