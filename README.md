# The Endless Path 🌿
### An AI-Powered Choose-Your-Own-Adventure Game
*Built as a final project for Stanford's Code in Place 2026*

---

## What It Does

The Endless Path/Infinite Story is a text-based adventure game that never runs out of story. It starts with hand-written scenes — you're standing at the end of a road before a small brick building, with a stream to the south and a hill to the west — and as you explore, the story branches. When you wander somewhere new that hasn't been written yet, the game calls ChatGPT live to generate the next scene, including a fresh description and new choices. The adventure can branch infinitely.

---

## How to Run

**Requirements:** Python 3, access to the Code in Place IDE (which provides the `ai` module)

```bash
python infinite_story.py
```

You'll see the opening scene printed to the console. Type a number to make your choice and press Enter. The story continues from there.

---

## Project Structure

```
├── infinite_story.py       # Main game file (Milestones 2–5)
├── warmup.py               # Dead-end finder (Milestone 1)
├── main.py                 # Ethics reflection (Milestone 6)
├── original_big.json       # Full pre-written story data
├── original_small.json     # Smaller story for testing
└── engineer_story.json     # Story used for ethics analysis
```

---

## How It Works

### 1. Story Structure
Story data is stored as a nested dictionary (loaded from JSON). Each scene has:
- `"text"` — the scene description printed to the player
- `"scene_summary"` — a short summary (used for history tracking)
- `"choices"` — a list of options, each with display text and a `scene_key` pointing to the next scene

### 2. The Game Loop
The main loop tracks `current_key` (starting at `"start"`). Each iteration:
1. Looks up the scene for `current_key`
2. Prints the scene text and numbered choices
3. Gets a valid choice from the user (re-prompts on invalid input)
4. Updates `current_key` to the chosen scene's key

### 3. AI Scene Generation
When `current_key` doesn't exist in the story data (a "dead end"), the game:
1. Prints `[Suspenseful music plays as the story continues...]`
2. Builds a prompt for ChatGPT including the missing key, an example scene format, and the overall plot
3. Calls `call_gpt()` and parses the JSON response
4. Saves the new scene into `story_data` so it's consistent if revisited
5. Continues the loop with the newly generated scene

### 4. Error Handling
ChatGPT occasionally returns malformed or empty JSON. The generation function retries up to 3 times, and if all attempts fail, falls back to a safe hardcoded scene — so the game never crashes mid-play.

---

## Key Concepts Used

- **Dictionaries** — nested JSON story data, scene lookup by key
- **Lists** — choices per scene, enumeration for numbered display
- **Loops** — main game loop, input validation loop, retry loop
- **Functions** — `print_scene`, `get_choice`, `generate_scene`, `process_response`
- **File reading** — `json.load` to load story data from disk
- **APIs** — `call_gpt` to generate new scenes via ChatGPT

---

## Ethics Reflection

As part of Milestone 6, the project explores the ethical implications of using generative AI in storytelling. Running `engineer_story.json` (a single-scene office story) reveals that ChatGPT consistently generates co-worker names that skew heavily toward Western, English-speaking regions — names like Sam, Lisa, Mark, Sarah, Tom — despite the global diversity of the world's population. This reflects biases embedded in the model's training data.

This raises real questions: if the same naming bias showed up in an AI system evaluating job candidates rather than generating story characters, it could systematically disadvantage equally qualified people with non-Western names — a form of algorithmic discrimination that's hard to detect precisely because it's baked into the training data rather than any explicit rule.

---

## Extensions Implemented

- **Retry logic** — retries `call_gpt` up to 3 times on malformed JSON before falling back
- **Graceful fallback** — never crashes; falls back to a safe scene if all retries fail
- **`strict=False` JSON parsing** — handles control characters in ChatGPT responses that would otherwise break standard JSON parsing

---

## Demo & Links
 
| | |
|---|---|
| 🎥 **YouTube Demo** | [Watch here](https://youtu.be/CooKhvH4nCM) |
| 🔗 **Project Link** | [Run on Code in Place IDE](https://codeinplace.stanford.edu/cip6/share/yM8P3xwEAwmsRmH9oHrV) |
 
---

## Credits

Assignment designed by Chris Piech, inspired by Eric Roberts.
Handout written with Anjali Sreenivas, Yasmine Alonso, Katie Liu.
Ethics by Javokhir Arifov and Dan Webber.
Part of Stanford's Code in Place 2025.
