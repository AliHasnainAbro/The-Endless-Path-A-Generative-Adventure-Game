import json
from ai import call_gpt

def print_scene(scene):
    print(scene["text"])
    for i, choice in enumerate(scene["choices"], start=1):
        print(f"{i}. {choice['text']}")

def get_choice(scene):
    num_choices = len(scene["choices"])
    choice = input("What do you choose? ")
    while not choice.isdigit() or not (1 <= int(choice) <= num_choices):
        choice = input("Please enter a valid choice: ")
    return int(choice)

def process_response(response):
    if response.startswith("```json"):
        response = response[7:-3]
    return json.loads(response, strict=False)
    
def generate_scene(scene_key, story_data):
    print("[Suspenseful music plays as the story continues...]")
    plot = story_data["plot"]
    example_scene = story_data["scenes"]["start"]
    prompt = (
        f"Return the next scene of a story for key {scene_key}. "
        f"An example scene should be formatted in json like this: {str(example_scene)}. "
        f"The main plot line of the story is {plot}. "
        f"Respond with ONLY valid JSON, no extra text or explanation."
    )

    for attempt in range(3):
        response = call_gpt(prompt)
        try:
            new_scene = process_response(response)
            story_data["scenes"][scene_key] = new_scene
            return new_scene
        except json.JSONDecodeError:
            continue

    fallback_scene = {
        "text": "You pause for a moment, taking in your surroundings before deciding how to proceed.",
        "scene_summary": "A brief pause before continuing the journey.",
        "choices": [
            {"text": "Continue forward", "scene_key": "start"},
            {"text": "Take a different path", "scene_key": "next_to_gully"}
        ]
    }
    
    story_data["scenes"][scene_key] = fallback_scene
    return fallback_scene

def main():
    story_data = json.load(open('original_big.json'))
    current_key = "start"

    while True:
        print()
        if current_key not in story_data["scenes"]:
            scene = generate_scene(current_key, story_data)
        else:
            scene = story_data["scenes"][current_key]
        print_scene(scene)
        choice = get_choice(scene)
        current_key = scene["choices"][choice - 1]["scene_key"]

if __name__ == "__main__":
    main()