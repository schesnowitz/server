https://cloud.linode.com/

https://git-scm.com/download/win

**point domain to linode**
https://www.linode.com/community/questions/18941/how-to-point-domain-to-linode

**set up sudo user**
```
adduser username

adduser username sudo
 
ssh username@123.45.6.789
```

**generate a key**
```
ssh-keygen
```
**view the key**
```
cat ~/.ssh/id_rsa.pub
```
**update and upgrade**
```
sudo apt update && sudo apt upgrade -y
```
**Install apache**
```
sudo apt install apache2 
```
**Install Python 3 WSGI adapter module for Apache**
```
sudo apt install libapache2-mod-wsgi-py3
```
**start apache**
```
sudo systemctl start apache2
```
**enable apache**
```
sudo systemctl enable apache2
```
**get apache status**
```
sudo systemctl status apache2
```
**apache commands**
```
sudo systemctl start apache2 

sudo systemctl stop apache2 

sudo systemctl restart apache2 

sudo systemctl reload apache2 

sudo systemctl status apache2 

sudo systemctl enable apache2

sudo apachectl configtest 
```
**Install venv**
```
sudo apt install python3-venv 
```
**Install pip**
```
sudo apt install python3-pip
```
**Create a virtual environment**
```
python3 -m venv environment
```
**Activate the virtual environment**
```
source var/www/project/environment/bin/activate
```

**Apache configuration file**
```
<VirtualHost *:80>
    ServerAdmin some_name@domain.com
    ServerName domain.com
    ServerAlias www.domain.com

    DocumentRoot /var/www/folder_name/

    ErrorLog ${APACHE_LOG_DIR}/domain.com_error.log
    CustomLog ${APACHE_LOG_DIR}/domain.com_access.log combined

    Alias /static /var/www/folder_name/static
    <Directory /var/www/folder_name/static>
            Require all granted
    </Directory>

    Alias /media /var/www/folder_name/media
    <Directory /var/www/folder_name/media>
            Require all granted
     </Directory>


    Alias /staticfiles /var/www/folder_name/staticfiles
    <Directory /var/www/folder_name/staticfiles>
            Require all granted
     </Directory>

    <Directory /var/www/folder_name/core>
            <Files wsgi.py>
                    Require all granted
            </Files>
    </Directory>

    WSGIDaemonProcess process_name python-path=/var/www/folder_name python-home=/var/www/folder_name/environment
    WSGIProcessGroup django_app
    WSGIScriptAlias / /var/www/folder_name/core/wsgi.py
</VirtualHost>    
```

**disable conf**
```
a2dissite 000-default.conf 
```
**enable conf**
```
a2ensite django_conf_file_name.conf
```