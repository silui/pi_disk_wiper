Script that wipes all new drive that is pluged into usb
Built in led will start blinking after disk have been wiped

added two lines in /etc/rc.local to gain control on onboard LED
```
sudo echo none > /sys/class/leds/led0/trigger
sudo chmod 777 /sys/class/leds/led0/brightness
```


Enable onboard led
```
echo none > /sys/class/leds/led0/trigge
```
Disable onboard led
```
echo mmc0 > /sys/class/leds/led0/trigge
```
