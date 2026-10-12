# Win11_Unattended.Xml_Toolkit

Automatic Windows 11 Pro installs with `autounattend.xml` answer files, made with the [Schneegans unattend generator](https://schneegans.de/windows/unattend-generator/).

In this repo I post the latest XML files I use to install Windows 11. There are many reasons you might need them, but the main one is that they drastically reduce installation time by automatically answering the questions the installer and OOBE ask you every time you install the OS.

I made these files because I got tired of clicking through OOBE and setting up accounts by hand on every install, so I put together an automated config with the Schneegans generator. I tested it on a Ryzen 7 laptop over USB 2.0: a full install to a ready-to-use desktop took about 20 minutes (drivers still need to be added separately afterward).

I'm not forcibly debloating Windows 11 with these files, as that could break some Windows features.

Before you use any file, read the [guide]

https://github.com/thunderstorm2kN/Win11_Unattended.Xml_Toolkit/blob/main/Warnings%20and%20operation%20procedures%20of%20the%20scripts


These tools are highly automatic. Installation starts as soon as you click **Next** on the disk selection screen, so double-check the disk you select. Careless use can cause data loss.

What's in the files

The online and offline versions install **Windows 11 Pro** with keyboard layouts for **English (US), Romanian and Norwegian**. The display language stays English (US).

The bypasses for the hardware requirements (TPM, Secure Boot and RAM) are simply ignored by the installer if your system is officially supported by Windows 11.

 What to expect

After installation, OOBE asks you for a network connection (choose "I don't have network" for the offline version, or connect to Wi-Fi/LAN for the online version) and for a username and password for the local account. The password is optional: you can click Next to leave it empty, and then you won't need a password to unlock or start your Windows 11 laptop.

After this, Windows starts updating, which depends on your internet speed. The online version usually restarts around 3 times (since Windows installs updates and newer drivers) and then lets you into the Windows 11 desktop with its normal UI.

The offline version skips the update process and makes writing Windows 11 to disk faster, but you'll still need to wait for Windows Update afterward, since that's how most drivers get installed. In my opinion this makes the overall process more automatic.

The full step-by-step instructions, including how to prepare the USB stick, are in the

https://github.com/thunderstorm2kN/Win11_Unattended.Xml_Toolkit/blob/main/Warnings%20and%20operation%20procedures%20of%20the%20scripts

Try it in a virtual machine

The Schneegans website can wrap the XML files into an `.iso`, which lets you use the files of this project on any virtual machine (as in the video below, using Oracle VirtualBox).

See how it works:

- Video: [TikTok demo] (https://vm.tiktok.com/ZN8MoXddh/)

- Step-by-step screenshots: [screenshots folder]
  https://github.com/thunderstorm2kN/Win11_Unattended.Xml_Toolkit/tree/main/screenshots

Bugs

If I find a bug, I'll report it in the [File with bugs] https://github.com/thunderstorm2kN/Win11_Unattended.Xml_Toolkit/blob/main/The%20%22Bugs%22%20file

Disclaimer

I do not assume responsibility for any damages or data loss. However, I can promise that everything posted here was tested at least once installing Windows 11 on one of my ASUS Vivobook laptops (both AMD and Intel platforms).

If you've made it this far, thank you for using my version of this software.

Credits

Answer files generated with Christoph Schneegans' [Unattend Generator](https://schneegans.de/windows/unattend-generator/).
