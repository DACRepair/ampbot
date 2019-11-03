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

| ENV | Usage |
| TOKEN | Discord Token |
| MESSAGE | The message it will send to the channel |
| DELETE | Deletes the message (`true` or `false`) |
| POLR_URL | URL Base to a Polr URL Shortener instance |
| POLR_KEY | API Key to Polr URL Shortener |

Message Tokens:
| Token | Value |
| `{name}` | A mention replacement for the users name |
| `{url}` | the AMP url |