# i stole from moonly - https://github.com/M-oonly/Moonly-Restarter
import requests
import subprocess
import json

with open('settings.json', 'r') as f:
  data = json.load(f)

webhook = data["webhookUrl"]
minutes_per_restart = data["minutes"]
webhookMsg = data["webhookMsg"]

embed_data = {
    "color": 5793266,
    "author": {
        "name": f"{webhookMsg}"
    }
}

while True:
    process = subprocess.Popen(['python', 'main.py'])
    requests.post(webhook, json={"content": None, "embeds": [embed_data]})
    try:
        process.wait(minutes_per_restart * 60)
    except KeyboardInterrupt:
        print("Exiting")
        break
    except Exception:
        pass
    process.kill()
    print("Restarting")
    continue
