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

Message Tokens:
| Token | Value |
| `{name}` | A mention replacement for the users name |
| `{url}` | the AMP url |