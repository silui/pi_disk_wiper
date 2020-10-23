import subprocess
import blkinfo
from time import sleep


filters = {"tran":"usb"}


led_state = 1
def trigger_led():
    global led_state
    led_state = not led_state
    print(str(int(led_state)))
    with open('/sys/class/leds/led0/brightness','w') as led:
        led.write(str(int(led_state)))

while True:
    disks = blkinfo.BlkDiskInfo().get_disks(filters)
    if disks:
        print("detected drive")
        target_disk_letter = disks[0].get("kname")
        subprocess.check_output(["sudo", "wipefs", "-a", "-f", "/dev/{}".format(target_disk_letter)])
        while blkinfo.BlkDiskInfo().get_disks(filters):
            trigger_led()
            sleep(0.5)
            trigger_led()
            sleep(0.5)
    sleep(3)