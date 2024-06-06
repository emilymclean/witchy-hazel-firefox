import json
import re
import os

def rgb_to_chrome(rgb):
    rgb = rgb[len("rgb("):-1]
    return [int(c) for c in re.split(", *", rgb)]

def rewrite():
    with open("manifest.json", "r") as file:
        input_file = file.read()
    input = json.loads(input_file)

    input["manifest_version"] = 3
    input["version"] = re.sub("[^\\d\\.]","",input["version"])
    input["theme"]["colors"] = {k: rgb_to_chrome(v) for k,v in input["theme"]["colors"].items()}

    if not os.path.exists("chrome"):
        os.makedirs("chrome")
    with open("chrome/manifest.json", "w") as file:
        file.write(json.dumps(input, indent=4))

if __name__ == "__main__":
    rewrite()