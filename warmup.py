import json

def main():
    story_data = json.load(open('original_small.json'))
    for scene_key, scene in story_data["scenes"].items():
        for choice in scene["choices"]:
            target = choice["scene_key"]
            if target not in story_data["scenes"]:
                print(target)

    print(story_data["plot"])
    print(story_data["scenes"]["start"]["text"])
    print(story_data["scenes"]["start"]["choices"][0]["scene_key"])

if __name__ == "__main__":
    main()