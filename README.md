# Modem HAT for the Raspberry Pi

This HAT is a modem that connects the Raspberry Pi to a plain old analog telephone line.

![Render of Modem HAT](images/modem-hat-2022-05-08-render.png)

The modem presents itself to the Raspberry Pi on UART4 and is controlled with the classic AT command set. It supports various standards (V.22bis, V.32bis, V.34, V.90, ...) at speeds of up to 56 kbps.

The design is based on a [Skyworks ISOmodem](https://www.skyworksinc.com/en/Products/Modems-and-DAAs/Data-and-Voice-Modems) chipset, specifically [Si2457](https://www.skyworksinc.com/en/Products/Modems-and-DAAs/Data-and-Voice-Modems/Si2457) data modem and Si3018 line side driver. The implementation
closely follows the circuits described in application note [AN93](https://www.skyworksinc.com/-/media/SkyWorks/SL/documents/public/application-notes/AN93.pdf).

**NOTE: Whatever your jurisdiction, we're pretty positive that connecting this device to the public phone system IS NOT LEGAL! Don't blame us if you get into trouble.**

## Raspberry Pi Configuration

The modem connects to the Raspberry Pi UART4 and requires CTS and RTS for flow control. To enable UART4 with CTS/RTS, edit `/boot/config.txt` and add the following line:

`dtoverlay=uart4,ctsrts`

After rebooting the Raspberry Pi, UART4 will be mapped to `/dev/ttyAMAx`, where `x` depends on the number of enabled UARTs. Typically, if only UART0 and UART4 are enabled, UART4 will be on `/dev/ttyAMA1`.

The modem is configured for automatic baudrate detection, supporting any standard DTE rate up to 307.2 kps.

## Modem Reset

Before first use after power-up, the modem must be reset by the Raspberry Pi.

To reset the modem, GPIO25 (pin 22) is set low for at least 500ms, then set high, followed by a delay of at least 300ms. This can be done with the following Python script.

```
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
GPIO.output(25, GPIO.LOW)
time.sleep(0.5)
GPIO.output(25, GPIO.HIGH)
time.sleep(0.3)
```

By default, the modem is configured for operation in the United States. For other countries the modem will need to be reconfigured after reset. See [AN93](https://www.skyworksinc.com/-/media/SkyWorks/SL/documents/public/application-notes/AN93.pdf) chapter 6.2 for details. 

## AT Command Set

The modem supports the [basic Hayes command set](https://en.wikipedia.org/wiki/Hayes_command_set#The_basic_Hayes_command_set).

For a complete list of supported AT commands as well as configuration registers refer to [AN93](https://www.skyworksinc.com/-/media/SkyWorks/SL/documents/public/application-notes/AN93.pdf) chapters 5.4 through 5.7. 

## Raspberry Pi GPIO Pinout

Required connections:
|Pin|Description|
|-|-|
|1|3.3V power for modem chipset|
|2,4|5V power for audio amplifier|
|19|UART4 CTS|
|21|UART4 RX|
|22|Modem reset, RPi GPIO25|
|23|UART4 RTS|
|24|UART4 TX|

Optional connections:
|Pin|Description|
|-|-|
|13|Modem interrupt, RPi GPIO27|
|15|Modem boot config EEPROM SDIO, RPi GPIO22|
|16|Modem boot config EEPROM CS, RPi GPIO23|
|18|Modem boot config EEPROM CLK, Rpi GPIO24|
|27|RPi config EEPROM SDA|
|28|RPi config EEPROM SCL|

Usually the modem boot config and interrupt pins are not electrically connected to the Rasbperry Pi GPIO header. Populate R29-R32 with 0-ohm resistors to use these pins.
