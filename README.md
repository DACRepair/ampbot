# NO AMP Bot
## Running
NoAmpBot is designed to run in docker.
```bash
docker run -d -it \
    -e TOKEN="Your Discord Token" \
    -e MESSAGE="The message you want sent to the channel" \
    dacepair/ampbot
```
Env Vars:

| ENV | Usage | Default |
| --- | --- | --- |
| TOKEN | Discord Token | |
| MESSAGE | The message it will send to the channel | *see dockerfile* |
| DELETE | Deletes the message (`true` or `false`) | false |
| POLR_URL | URL Base to a Polr URL Shortener instance. If left blank it will disable this feature. | |
| POLR_KEY | API Key to Polr URL Shortener | |

Message Tokens:

| Token | Value |
| --- | --- |
| `{name}` | A mention replacement for the users name |
| `{url}` | the AMP url |