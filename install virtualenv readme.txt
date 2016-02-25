How to install Django on Windows¶

This document will guide you through installing Python 3.5 and Django on Windows. It also provides instructions for installing virtualenv and virtualenvwrapper, which make it easier to work on Python projects. This is meant as a beginner’s guide for users working on Django projects and does not reflect how Django should be installed when developing patches for Django itself.

The steps in this guide have been tested with Windows 7, 8, and 10. In other versions, the steps would be similar. You will need to be familiar with using the Windows command prompt.

Install Python¶

Django is a Python web framework, thus requiring Python to be installed on your machine. At the time of writing, Python 3.5 is the latest version.

To install Python on your machine go to https://python.org/downloads/. The website should offer you a download button for the latest Python version. Download the executable installer and run it. Check the box next to Add Python 3.5 to PATH and then click Install Now.

After installation, open the command prompt and check that the Python version matches the version you installed by executing:

python --version
About pip¶

pip is a package manage for Python. It makes installing and uninstalling Python packages (such as Django!) very easy. For the rest of the installation, we’ll use pip to install Python packages from the command line.

Install virtualenv and virtualenvwrapper¶

virtualenv and virtualenvwrapper provide a dedicated environment for each Django project you create. While not mandatory, this is considered a best practice and will save you time in the future when you’re ready to deploy your project. Simply type:

pip install virtualenvwrapper-win
Then create a virtual environment for your project:

mkvirtualenv myproject
The virtual environment will be activated automatically and you’ll see “(myproject)” next to the command prompt to designate that. If you start a new command prompt, you’ll need to activate the environment again using:

workon myproject
Install Django¶

Django can be installed easily using pip.

In the command prompt, execute the following command:

pip install django
This will download and install the latest Django release.

After the installation has completed, you can verify your Django installation by executing django-admin --version in the command prompt.

See Get your database running for information on database installation with Django.

Common pitfalls¶

If django-admin only displays the help text no matter what arguments it is given, there is probably a problem with the file association in Windows. Check if there is more than one environment variable set for running Python scripts in PATH. This usually occurs when there is more than one Python version installed.

If you are connecting to the internet behind a proxy, there might be problem in running the command pip install django. Set the environment variables for proxy configuration in the command prompt as follows:

set http_proxy=http://username:password@proxyserver:proxyport
set https_proxy=https://username:password@proxyserver:proxyport

my example:
Microsoft Windows [Version 10.0.10586]
(c) 2015 Microsoft Corporation. All rights reserved.

C:\WINDOWS\system32>cd c:\users


c:\Users\rholmes69>pip2 install virtualenvwrapper-win
Downloading/unpacking virtualenvwrapper-win
  Downloading virtualenvwrapper-win-1.2.1.zip
  Running setup.py (path:c:\users\rholme~1\appdata\local\temp\pip_build_rholmes69\virtualenvwrapper-win\setup.py) egg_info for package virtualenvwrapper-win

Requirement already satisfied (use --upgrade to upgrade): virtualenv in c:\python27\lib\site-packages (from virtualenvwrapper-win)
Installing collected packages: virtualenvwrapper-win
  Running setup.py install for virtualenvwrapper-win

Successfully installed virtualenvwrapper-win
Cleaning up...

c:\Users\rholmes69>mkdir testvirtualenv

c:\Users\rholmes69>cd testvirtualenv

c:\Users\rholmes69\testvirtualenv>mkvirtualenv myproject
Using base prefix 'd:\\program files\\python35'
New python executable in C:\Users\rholmes69\Envs\myproject\Scripts\python.exe
Installing setuptools, pip, wheel...done.

(myproject) c:\Users\rholmes69\testvirtualenv>workon myproject
(myproject) c:\Users\rholmes69\testvirtualenv>pip install django
Collecting django
  Using cached Django-1.9.2-py2.py3-none-any.whl
Installing collected packages: django
Successfully installed django-1.9.2

(myproject) c:\Users\rholmes69\testvirtualenv>django-admin --version
1.9.2

(myproject) c:\Users\rholmes69\testvirtualenv>