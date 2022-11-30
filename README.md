<h1 align="center">JAWHEAD FIND ALL SOCIAL MEDIA ACCOUNTS WITH A USERNAME!</h1>

# Can be installed in any linux system or in termux

## Before installation:
* You need git,python3 and requests module installed on your linux/termux
* most of the linux machines comes with pre-installed git,python3 and requests module 
## if they are not installed, install it by:
* for linux:
    - install git from [here](https://linuxhint.com/install-use-git-linux/) 
    - install python3 from [here](https://www.python.org/downloads/) 
    - [click here](https://www.tecmint.com/install-pip-in-linux/) for installing pip 
    - then install requests module by running:
```shell script
pip3 install requests
```
* for termux:

**Open termux and run**
```shell script
apt update && apt full-upgrade
```
```shell script
pkg install python
```
```shell script
pkg install git
```
```shell script
apt update && apt full-upgrade
```
```shell script
pip install requests
pip2 install requests
```
# Installation in Linux:
**Open terminal and run:**
```shell script
git clone https://github.com/poisk-ls/jawhead
```
```shell script
cd jawhead
```
```shell script
bash install.sh
```
* Now jawhead is Succesfully installed in your system
# Installation in Termux:
**Open termux and type:**
```shell script
git clone https://github.com/poisk-ls/jawhead
```
```shell script
cd jawhead
```
```shell script
bash termux-install.sh
```
* Now Aliens_eye is Succesfully installed in your termux
## To uninstall in linux:
```shell script
cd jawhead
```
```shell script
bash uninstall.sh
```
* done!
## To uninstall in Termux:
```shell script
cd jawhead
```
```shell script
bash termux-uninstall.sh
```
* done!
# Usage :
```shell script
jawhead <username>
```
### Example :
```shell script
jawhead blackh4t
```
## You can also search multiple accounts by enter the usernames separated by space
### Example :
```shell script
jawhead blackhat john32 jake12
```
# Or:
```shell script
jawhead
```
### Then enter the username
## The collected data will be saved in username.json
## Enjoy!
