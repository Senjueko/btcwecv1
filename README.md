# btcwecv1

## PURPOSE 
Purpose of this project is getting data from specific website using selenium and print out regularly. Also parsing data to JSON form.

## INSTALLATION 
You should have python3, Selenium and Selenium's Firefox driver to execute this project.

#### **Installing Selenium**
1. You can install Python virtualenv module globally using PIP 3 as follows: ***$ sudo pip3 install virtualenv***
2. Create a project directory selenium-firefox/ in your current working directory as follows: ***$ mkdir -pv selenium-firefox/drivers***
3. Navigate to your newly created project directory selenium-firefox/ as follows: ***$ cd selenium-firefox/***
4. Create a Python virtual environment in your project directory with the following command: ***$ virtualenv .venv***
5. Activate the Python virtual environment from your project directory with the following command: ***$ source .env/bin/activate***
6. You can install Selenium Python library using PIP 3 as follows: ***$ pip3 install selenium***
7. To download the Firefox Gecko Driver, visit the GitHub releases page of ***https://github.com/mozilla/geckodriver/releases/tag/v0.29.1*** from your favorite web browser.   
8. To download the Firefox Gecko Driver, scroll down a little bit and click on the Linux geckodriver tar.gz archive depending on your operating system architecture.
    * If you’re using a 32-bit operating system, click on the geckodriver-v0.26.0-linux32.tar.gz link.
    * If you’re using a 64-bit operating system, click on the geckodriver-v0.26.0-linuxx64.tar.gz link.
9. You can extract the geckodriver-v0.26.0-linux64.tar.gz archive from the ~/Downloads directory to the drivers/ directory of your project with the following command: ***$ tar -xzf ~/Downloads/geckodriver-v0.26.0-linux64.tar.gz -C drivers/***

Reference URL: https://linuxhint.com/using_selenium_firefox_driver/

#### **Installing BeautifulSoup**
1. Run the following command on terminal: ***sudo apt-get update***
2. After that run this: ***sudo apt-get install python-beautifulsoup***

## HOW TO USE??
Open the terminal and type "python3 main.py" (main folder must be at same location with your working space)
