# Usage

At first run you must follow auth link and get auth key. Then you can add this command to crontab file.

```bash
$ cd /your-folder-for-reports/sc-crawl-errors && python -m sc-crawl-errors.main -u https://repka.ua -c notFound -p web --noauth_local_webserver
```
