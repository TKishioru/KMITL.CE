## Chocolatey
https://docs.chocolatey.org/en-us/choco/setup

## Meteor
https://www.meteor.com/developers/install
https://react-tutorial.meteor.com/simple-todos/01-creating-app.html
http://courses.ics.hawaii.edu/ics314f18/morea/meteor-1/reading-meteor-tips-windows.html
- ติดตั้ง Linux บน Window
```
ON PowerShell (Admin mode)

wsl --install
```
```
Microsoft Windows [Version 10.0.19044.1645]
(c) Microsoft Corporation. All rights reserved.
                                                                                                                        C:\WINDOWS\system32>@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"                                                                                                                      Forcing web requests to allow TLS v1.2 (Required for requests to Chocolatey.org)                                        Getting latest version of the Chocolatey package for download.
Not using proxy.
Getting Chocolatey from https://community.chocolatey.org/api/v2/package/chocolatey/1.1.0.
Downloading https://community.chocolatey.org/api/v2/package/chocolatey/1.1.0 to C:\Users\khamp\AppData\Local\Temp\chocolatey\chocoInstall\chocolatey.zip
Not using proxy.
Extracting C:\Users\khamp\AppData\Local\Temp\chocolatey\chocoInstall\chocolatey.zip to C:\Users\khamp\AppData\Local\Temp\chocolatey\chocoInstall
Installing Chocolatey on the local machine
Creating ChocolateyInstall as an environment variable (targeting 'Machine')
  Setting ChocolateyInstall to 'C:\ProgramData\chocolatey'
WARNING: It's very likely you will need to close and reopen your shell
  before you can use choco.
Restricting write permissions to Administrators
We are setting up the Chocolatey package repository.
The packages themselves go to 'C:\ProgramData\chocolatey\lib'
  (i.e. C:\ProgramData\chocolatey\lib\yourPackageName).
A shim file for the command line goes to 'C:\ProgramData\chocolatey\bin'
  and points to an executable in 'C:\ProgramData\chocolatey\lib\yourPackageName'.

Creating Chocolatey folders if they do not already exist.

WARNING: You can safely ignore errors related to missing log files when
  upgrading from a version of Chocolatey less than 0.9.9.
  'Batch file could not be found' is also safe to ignore.
  'The system cannot find the file specified' - also safe.
chocolatey.nupkg file not installed in lib.
 Attempting to locate it from bootstrapper.
PATH environment variable does not have C:\ProgramData\chocolatey\bin in it. Adding...
WARNING: Not setting tab completion: Profile file does not exist at
'C:\Users\khamp\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1'.
Chocolatey (choco.exe) is now ready.
You can call choco from anywhere, command line or powershell by typing choco.
Run choco /? for a list of functions.
You may need to shut down and restart powershell and/or consoles
 first prior to using choco.
Ensuring Chocolatey commands are on the path
Ensuring chocolatey.nupkg is in the lib folder

C:\WINDOWS\system32>choco upgrade chocolatey
Chocolatey v1.1.0
2 validations performed. 1 success(es), 1 warning(s), and 0 error(s).

Validation Warnings:
 - A pending system reboot request has been detected, however, this is
   being ignored due to the current Chocolatey configuration.  If you
   want to halt when this occurs, then either set the global feature
   using:
     choco feature enable -name=exitOnRebootDetected
   or pass the option --exit-when-reboot-detected.

Upgrading the following packages:
chocolatey
By upgrading, you accept licenses for the packages.
chocolatey v1.1.0 is the latest version available based on your source(s).

Chocolatey upgraded 0/1 packages.
 See the log for details (C:\ProgramData\chocolatey\logs\chocolatey.log).

C:\WINDOWS\system32>choco install meteor
Chocolatey v1.1.0
2 validations performed. 1 success(es), 1 warning(s), and 0 error(s).

Validation Warnings:
 - A pending system reboot request has been detected, however, this is
   being ignored due to the current Chocolatey configuration.  If you
   want to halt when this occurs, then either set the global feature
   using:
     choco feature enable -name=exitOnRebootDetected
   or pass the option --exit-when-reboot-detected.

Installing the following packages:
meteor
By installing, you accept licenses for the packages.
Progress: Downloading chocolatey-core.extension 1.4.0... 100%
Progress: Downloading chocolatey-compatibility.extension 1.0.0... 100%
Progress: Downloading meteor 0.0.5... 100%

chocolatey-compatibility.extension v1.0.0 [Approved]
chocolatey-compatibility.extension package files install completed. Performing other installation steps.
 Installed/updated chocolatey-compatibility extensions.
 The install of chocolatey-compatibility.extension was successful.
  Software installed to 'C:\ProgramData\chocolatey\extensions\chocolatey-compatibility'

chocolatey-core.extension v1.4.0 [Approved]
chocolatey-core.extension package files install completed. Performing other installation steps.
 Installed/updated chocolatey-core extensions.
 The install of chocolatey-core.extension was successful.
  Software installed to 'C:\ProgramData\chocolatey\extensions\chocolatey-core'

meteor v0.0.5 [Approved]
meteor package files install completed. Performing other installation steps.
The package meteor wants to run 'chocolateyinstall.ps1'.
Note: If you don't run this script, the installation will fail.
Note: To confirm automatically next time, use '-y' or consider:
choco feature enable -n allowGlobalConfirmation
Do you want to run the script?([Y]es/[A]ll - yes to all/[N]o/[P]rint): Y

WARNING: No registry key found based on  'Meteor'

C:\WINDOWS\system32>
C:\WINDOWS\system32> meteor --version
'"C:\Users\khamp\AppData\Local\.meteor\\packages\meteor-tool\2.7.0\mt-os.windows.x86_64\meteor.bat"' is not recognized as an internal or external command,
operable program or batch file.

C:\WINDOWS\system32>choco install meteor
Chocolatey v1.1.0
2 validations performed. 1 success(es), 1 warning(s), and 0 error(s).

Validation Warnings:
 - A pending system reboot request has been detected, however, this is
   being ignored due to the current Chocolatey configuration.  If you
   want to halt when this occurs, then either set the global feature
   using:
     choco feature enable -name=exitOnRebootDetected
   or pass the option --exit-when-reboot-detected.

Installing the following packages:
meteor
By installing, you accept licenses for the packages.
meteor v0.0.5 already installed.
 Use --force to reinstall, specify a version to install, or try upgrade.

Chocolatey installed 0/1 packages.
 See the log for details (C:\ProgramData\chocolatey\logs\chocolatey.log).

Warnings:
 - meteor - meteor v0.0.5 already installed.
 Use --force to reinstall, specify a version to install, or try upgrade.

C:\WINDOWS\system32> meteor --version
'"C:\Users\khamp\AppData\Local\.meteor\\packages\meteor-tool\2.7.0\mt-os.windows.x86_64\meteor.bat"' is not recognized as an internal or external command,
operable program or batch file.

C:\WINDOWS\system32>choco --version
1.1.0

C:\WINDOWS\system32>meteor
'"C:\Users\khamp\AppData\Local\.meteor\\packages\meteor-tool\2.7.0\mt-os.windows.x86_64\meteor.bat"' is not recognized as an internal or external command,
operable program or batch file.

C:\WINDOWS\system32>meteor --versoin
'"C:\Users\khamp\AppData\Local\.meteor\\packages\meteor-tool\2.7.0\mt-os.windows.x86_64\meteor.bat"' is not recognized as an internal or external command,
operable program or batch file.

C:\WINDOWS\system32>meteor --version
'"C:\Users\khamp\AppData\Local\.meteor\\packages\meteor-tool\2.7.0\mt-os.windows.x86_64\meteor.bat"' is not recognized as an internal or external command,
operable program or batch file.

C:\WINDOWS\system32>meteor --version
The system cannot find the path specified.

C:\WINDOWS\system32>meteor --version
The system cannot find the path specified.

C:\WINDOWS\system32>choco install meteor
Chocolatey v1.1.0
2 validations performed. 1 success(es), 1 warning(s), and 0 error(s).

Validation Warnings:
 - A pending system reboot request has been detected, however, this is
   being ignored due to the current Chocolatey configuration.  If you
   want to halt when this occurs, then either set the global feature
   using:
     choco feature enable -name=exitOnRebootDetected
   or pass the option --exit-when-reboot-detected.

Installing the following packages:
meteor
By installing, you accept licenses for the packages.
meteor v0.0.5 already installed.
 Use --force to reinstall, specify a version to install, or try upgrade.

Chocolatey installed 0/1 packages.
 See the log for details (C:\ProgramData\chocolatey\logs\chocolatey.log).

Warnings:
 - meteor - meteor v0.0.5 already installed.
 Use --force to reinstall, specify a version to install, or try upgrade.

C:\WINDOWS\system32>meteor
The system cannot find the path specified.

C:\WINDOWS\system32>meteor --
The system cannot find the path specified.

C:\WINDOWS\system32>choco install meteor --force
Chocolatey v1.1.0
2 validations performed. 1 success(es), 1 warning(s), and 0 error(s).

Validation Warnings:
 - A pending system reboot request has been detected, however, this is
   being ignored due to the current Chocolatey configuration.  If you
   want to halt when this occurs, then either set the global feature
   using:
     choco feature enable -name=exitOnRebootDetected
   or pass the option --exit-when-reboot-detected.

Installing the following packages:
meteor
By installing, you accept licenses for the packages.
meteor v0.0.5 already installed. Forcing reinstall of version '0.0.5'.
 Please use upgrade if you meant to upgrade to a new version.

meteor v0.0.5 (forced) [Approved]
meteor package files install completed. Performing other installation steps.
The package meteor wants to run 'chocolateyinstall.ps1'.
Note: If you don't run this script, the installation will fail.
Note: To confirm automatically next time, use '-y' or consider:
choco feature enable -n allowGlobalConfirmation
Do you want to run the script?([Y]es/[A]ll - yes to all/[N]o/[P]rint): Y

WARNING: No registry key found based on  'Meteor'
Downloading meteor 64 bit
  from 'https://packages.meteor.com/bootstrap-link?arch=os.windows.x86_64'
Progress: 100% - Completed download of C:\Users\khamp\AppData\Local\Temp\chocolatey\meteor\0.0.5\meteor-bootstrap-os.windows.x86_64.tar.gz (316.82 MB).
Download of meteor-bootstrap-os.windows.x86_64.tar.gz (316.82 MB) completed.
Extracting C:\Users\khamp\AppData\Local\Temp\chocolatey\meteor\0.0.5\meteor-bootstrap-os.windows.x86_64.tar.gz to C:\Users\khamp\AppData\Local\Temp\chocolatey\meteor\0.0.5...
C:\Users\khamp\AppData\Local\Temp\chocolatey\meteor\0.0.5
Extracting C:\Users\khamp\AppData\Local\Temp\chocolatey\meteor\0.0.5\meteor-bootstrap-os.windows.x86_64.tar to C:\Users\khamp\AppData\Local...
C:\Users\khamp\AppData\Local
***************************************

Meteor has been installed!

To get started fast:

  $ meteor create ~/my_cool_app
  $ cd ~/my_cool_app
  $ meteor

Or see the docs at:

  https://docs.meteor.com

***************************************
 The install of meteor was successful.
  Software installed to 'C:\Users\khamp\AppData\Local'

Chocolatey installed 1/1 packages.
 See the log for details (C:\ProgramData\chocolatey\logs\chocolatey.log).

C:\WINDOWS\system32>Meteor
run: You're not in a Meteor project directory.

To create a new Meteor project:
  meteor create <project name>
For example:
  meteor create myapp

For more help, see 'meteor --help'.

C:\WINDOWS\system32>npm install -g meteor

changed 47 packages, and audited 48 packages in 5s

2 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities

C:\WINDOWS\system32>meteor --version
Meteor 2.7

C:\WINDOWS\system32>

-----------------
Microsoft Windows [Version 10.0.19044.1645]
(c) Microsoft Corporation. All rights reserved.

C:\WINDOWS\system32>meteor npm install
npm WARN saveError ENOENT: no such file or directory, open 'C:\WINDOWS\system32\package.json'
npm notice created a lockfile as package-lock.json. You should commit this file.
npm WARN enoent ENOENT: no such file or directory, open 'C:\WINDOWS\system32\package.json'
npm WARN system32 No description
npm WARN system32 No repository field.
npm WARN system32 No README data
npm WARN system32 No license field.

up to date in 0.465s
found 0 vulnerabilities


C:\WINDOWS\system32>meteor
run: You're not in a Meteor project directory.

To create a new Meteor project:
  meteor create <project name>
For example:
  meteor create myapp

For more help, see 'meteor --help'.

C:\WINDOWS\system32>meteor create mytest
Created a new Meteor app in 'mytest'.

To run your new app:
  cd mytest
  meteor

If you are new to Meteor, try some of the learning resources here:
  https://www.meteor.com/tutorials

When you’re ready to deploy and host your new Meteor application, check out Cloud:
  https://www.meteor.com/cloud


C:\WINDOWS\system32>cd mytest

C:\Windows\System32\mytest>meteor
[[[[[ C:\Windows\System32\mytest ]]]]]

=> Started proxy.
=> Started HMR server.
=> Started MongoDB.
=> Started your app.

=> App running at: http://localhost:3000/
   Type Control-C twice to stop.

```
## MongoDB 4.0.28
https://www.mongodb.com/try/download/community