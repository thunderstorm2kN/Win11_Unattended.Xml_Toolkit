# Making-win11-install-Authomatic
In this repo branch, I post the latest XML files I use to install Windows 11. There are many reasons you might need these — the main one being that these files drastically reduce Windows 11 installation time by automatically answering the questions the installer and OOBE ask you every time you install the OS. Made with the schneegans.de generator.

The main reason I made these files: I got tired of clicking through OOBE and manually setting up accounts every time I installed Windows, so I put together an automated config using the Schneegans unattend generator. Tested it on a Ryzen 7 laptop over USB 2.0 — full install to a ready-to-use desktop in about 20 minutes (drivers still need to be added separately afterward).

I am not forcibly debloating Windows 11 with the files I generated, as that could break some Windows 11 features.

The online and offline versions are meant to install Windows 11 Pro with language support for the following locales: English (US), Romanian, and Norwegian.

After installation, the script makes OOBE ask you for a network connection (choose "I don't have network" for the offline version, or connect to WiFi/LAN if using the online version), and to set up a username and password for the local account (password is not mandatory — you can click Next if you don't need one; the advantage is that you won't need a password to unlock/start your Windows 11 laptop anymore).

After updating, the online version will restart 3 times (since Windows installs updates and newer drivers) and then let you into enter the Windows 11 desktop with its normal UI.

Again, the offline version skips the update process and makes writing Windows 11 to disk faster, but you'll still need to wait a while for Windows updates afterward, since they're needed to install drivers (and this makes the overall process more automatic, in my opinion).

If you've made it this far, thank you for using my version of this software.

I remind you that I do not assume responsibility for any damages or data loss. However, I can promise that everything posted here was tested at least once installing Windows 11 on one of my ASUS Vivobook laptops (both on AMD and Intel platforms). 

If you need to use any versions the website ( https://schneegans.de/windows/unattend-generator/ ) lets you to wrap the XML files into an .iso file which ultimately enables you to use the files of this project on any Virtual Machine (as in the video I attached below using ORACLE Virtual box).

If I find a bug, I'll report it in the "File with bugs."

Note: If your system is officially supported by Windows 11, the bypasses in the code (for TPM, CPU generation, and RAM requirements) will simply be ignored by the installer.

Before using any of the scripts, please read the "Warnings and operation procedures of the scripts," as these tools are highly automatic and can result in loss of data if used carelessly. Thank you for your understanding!

Take a look on how it works via our TikTok video! 
https://vm.tiktok.com/ZN8MoXddh/

Also take a look at the screenshots folder to see how our script operates step-by-step. 
