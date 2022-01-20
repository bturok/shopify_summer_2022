# Shopify Backend Developer Intern Coding Challenge - Summer 2022
## Brandon Turok
### 19 January 2022

---

In order to run this application, you will need a VPS running Debian 11 "bullseye". These directions assume that your
VPS has a root account and no user accounts.

Run the following commands in the following order. Lines beginning with the # symbol are to be run as root, while lines 
beginning with the $ symbol are to be run as a user-level account:

    # apt update
    # apt -y upgrade
    # apt -y install python3 python3-venv python3-pip git sqlite3
    # adduser --disabled-password --gecos "" shopinternapp
    # su shopinternapp
    $ cd ~
    $ git clone https://github.com/bturok/shopify_summer_2022.git
    $ cd shopify_summer_2022/
    $ python3 -m venv venv/
    $ source venv/bin/activate
    $ pip install flask
    $ python3 ./init_db.py
    $ python3 ./app.py

Navigate to the URL displayed on the terminal to interact with the web app. For example, if the terminal displays
`Running on http://10.0.0.2:5000/` then you should visit that URL in your web browser.
