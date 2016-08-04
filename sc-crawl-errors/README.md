# Usage

Create your credentials in [Google API Manager](https://console.developers.google.com)

* Create credentials
* OAuth client ID
* Other
* Create

Then you will get Client ID and Client secret, such as:

`321691317947-rni5a5qaq81eknghj6acgsmu1jrepnjb.apps.googleusercontent.com`

`lQJC2A8scYKFIqUUFHFuDBHK`

Put them into configuration file:

`/usr/local/lib/python3.5/site-packages/sc-crawl-errors/client_secrets.json`

Then you can run:

```bash
$ cd /your-folder-for-reports/sc-crawl-errors && python -m sc-crawl-errors.main -u https://repka.ua -c notFound -p web --noauth_local_webserver
```

At the first run you must follow auth link and get auth key.

```bash
Go to the following link in your browser:

    https://accounts.google.com/o/oauth2/auth?redirect_uri=...&access_type=offline&response_type=code

Enter verification code: [[your key from the link above]]

Authentication successful.
```

Now you can add this command (for example) to crontab file.
