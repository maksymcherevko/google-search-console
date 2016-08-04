# Usage

```bash
$ cd /your-folder-for-reports/sc-crawl-errors && python -m sc-crawl-errors.main -u https://repka.ua -c notFound -p web --noauth_local_webserver
```

At first run you must follow auth link and get auth key.

```bash
Go to the following link in your browser:

    https://accounts.google.com/o/oauth2/auth?redirect_uri=...&access_type=offline&response_type=code

Enter verification code: [[your key from the link above]]

Authentication successful.
```

Then you can add this command to crontab file.
