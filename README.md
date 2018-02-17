# HANSHIN-Tigers-report
It tells you HANSHIN Tigers (Japanese STRONG Baseball Team) report.

## Requirements
HANSHIN-Tigers-report requires the following to run:

- Python 3.x

## Usage
Install python libraries:
```sh
$ pip install requests
$ pip install beautifulsoup4
$ pip install lxml
```

Clone software:
```sh
$ cd
$ git clone https://github.com/donchan922/HANSHIN-Tigers-report.git
```

Modify software:
```
$ vi ~/HANSHIN-Tigers-report/tigers_report.py

...

# replace YOUR-USER-AGENT to your User-Agent (ex. Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36)
headers = {'User-Agent': 'YOUR-USER-AGENT'}
```

Execute following command:
```sh
$ python ~/HANSHIN-Tigers-report/tigers_report.py
```

result (for example):
```sh
試合終了
阪神2 - 7巨人
```
Fight! Fight! HANSHIN Tigers!

## License
This software is released under the MIT License, see LICENSE.
