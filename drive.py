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
        target_disk_letter = disks[0].get("kname")
        print('detected{}'.format(target_disk_letter))
        subprocess.check_output(["sudo", "wipefs", "-a", "-f", "/dev/{}".format(target_disk_letter)])
        dd_cmd = ["sudo", "dd", "if=/dev/zero", "of=/dev/{}".format(target_disk_letter), "bs=512", "count=10240"]
        subprocess.check_output(dd_cmd, stderr=subprocess.STDOUT)
        sectors = int(subprocess.check_output(['sudo', 'blockdev', '--getsz', '/dev/{}'.format(target_disk_letter)]))
        subprocess.check_output(dd_cmd + ['seek={}'.format(sectors - 10240)], stderr=subprocess.STDOUT)

        while blkinfo.BlkDiskInfo().get_disks(filters):
            trigger_led()
            sleep(0.5)
            trigger_led()
            sleep(0.5)
    sleep(2)
