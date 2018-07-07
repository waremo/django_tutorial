# Polls Application in Django Tutorial

This archive is "Polls" application in "Writing your first Django app" 
at each stage:

| Date | Tag-Ver |description |
|:---:|:---:|:------|
| 2018-07-07 | func-0.9 | Function View, first release. <br>Roughly Corresponds to Part 4|


## Getting Started

The following instructions should be valid for any Linuxen and macOS. 

### Prerequisites

The mandatory commands and environment are:

* Ubuntu-16.04 or later, or macOS-10.12 or later

* Python: 3.5 or 3.6

* Django: 2.0.x

* git

The easiest way to build the environment is to use PyVenv.

```
fukuda@falcon:~% python3.6 -m venv pve366
zsh: correct 'pve366' to 'pve36' [nyae]? n
fukuda@falcon:~% cd pve366
fukuda@falcon:~/pve366% . bin/activate
(pve366) fukuda@falcon:~/pve366% pip install django
Successfully installed django-2.0.7 pytz-2018.5
.....
(pve366) fukuda@falcon:~/pve366% python -m django version
2.0.7
(pve366) fukuda@falcon:~/pve366% cd
(pve366) fukuda@falcon:~% mkdir test                                              
(pve366) fukuda@falcon:~% cd test
(pve366) fukuda@falcon:~/test% git clone git://github.com/waremo/django_tutorial.git
Cloning into 'django_tutorial'...
remote: Counting objects: 24, done.
remote: Compressing objects: 100% (21/21), done.
remote: Total 24 (delta 0), reused 24 (delta 0), pack-reused 0
Receiving objects: 100% (24/24), 10.65 KiB | 1.33 MiB/s, done.
(pve366) fukuda@falcon:~/test% cd django_tutorial 
(pve366) fukuda@falcon:~/test/django_tutorial% python manage.py runserver 0:8888
Performing system checks...

System check identified no issues (0 silenced).
July 07, 2018 - 19:25:46
Django version 2.0.7, using settings 'mysite.settings'
Starting development server at http://0:8888/
Quit the server with CONTROL-C.
[07/Jul/2018 21:04:35] "GET /polls/1/vote/ HTTP/1.1" 200 658
```

## Operation

As stated in the tutorial, accessing to `http://localhost:8888/index` 
would return the list of the questions.


