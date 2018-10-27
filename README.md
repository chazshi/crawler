# crawler
A crawler written in Python.

## error handle
1. Failed building wheel for Twisted...


    before you use `pip install scrapy` use this command:

    `$> pip install Twisted-18.7.0-cp36-cp36m-win_amd64.whl`

    Download the appropriate version → [pip whl](https://www.lfd.uci.edu/~gohlke/pythonlibs/)

2. Visual C++ 14.0 required
    
    click here → [Microsoft Support](https://support.microsoft.com/zh-cn/help/2977003/the-latest-supported-visual-c-downloads)

3. mysqlclient download failed
    

    use this file or search download and install:
    
    `$> pip install mysqlclient-1.3.13-cp36-cp36m-win_amd64.whl`
    
    Download the appropriate version → [pip whl](https://www.lfd.uci.edu/~gohlke/pythonlibs/)

4. _mysql_exceptions.OperationalError: (2059, <NULL>)
django.db.utils.OperationalError: (2059, <NULL>)


    `$> mysql -u root -p`

    `$> use mysql;`

    `$> alter user 'root'@'localhost' identified with mysql_native_password by '123456'; `
    
    `$> flush privileges;`
    
5. delete ./crawlerview/Infos/migrations/xxxx_initial.py
create database 'crawler'    
    `$> python ./crawlerview/manage.py makemigrations`
    
    `$> python ./crawlerview/manage.py migrate`


## HOW TO USE
`$> python main.py`

## 