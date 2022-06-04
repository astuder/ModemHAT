# Modem HAT for the Raspberry Pi

This HAT connects the Raspberry Pi to a plain old telephone line.

![Render of Modem HAT](images/modem-hat-2022-05-08-render.png)

The modem presents itself to the Raspberry Pi on UART4 and is controlled with the classic AT command set. It supports various standards (V.22bis, V.32bis, V.34, V.90, ...) at speeds of up to 56 kbps.

The design is based on a [Skyworks ISOmodem](https://www.skyworksinc.com/en/Products/Modems-and-DAAs/Data-and-Voice-Modems) chip set, specifically [Si2457](https://www.skyworksinc.com/en/Products/Modems-and-DAAs/Data-and-Voice-Modems/Si2457) data modem and Si3018 line side driver. The implementation
closely follows the circuits described in [AN93](https://www.skyworksinc.com/-/media/SkyWorks/SL/documents/public/application-notes/AN93.pdf).

**NOTE: Whatever your jurisdiction, we're pretty positive that connecting this device to the public phone system IS NOT LEGAL! Don't blame us if you get into trouble.**
