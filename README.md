# Teen-Trailblazer - A Ren'Py Visual Novel

Welcome to the **Teen-Trailblazer Game**! This interactive visual novel, built using **Ren'Py**, offers an engaging experience where players navigate through different career paths, face real-world scenarios, and make decisions that impact their journey.

## 🧑‍💻 About Ren'Py

[Ren'Py](https://www.renpy.org) is a popular visual novel engine that simplifies the process of creating interactive storytelling experiences. It supports branching narratives, character dialogue, and multimedia integration, making it a versatile choice for both novice and experienced game developers. With its user-friendly scripting language and customizable features, Ren'Py allows creators to design engaging stories like the Career Card Game, where player choices drive the narrative.

## 🚀 Features

- Choose from multiple career options like **Doctor**, **Civil Engineer**, **IPS Officer**, and **School Administrator**.
- Experience dynamic scenarios and face decision-making challenges.
- Track your progress through success, moderate performance, or failure outcomes.
- Interactive visuals and animations.

## 🛠️ Requirements

- [Ren'Py SDK](https://www.renpy.org/latest.html) (version 8.3.4 or later)
- Python 3.9 or higher
- Compatible OS: Windows, macOS, or Linux

## 🧑‍💻 Installation

1. Download and install the **Ren'Py SDK** from the official website: [Ren'Py SDK](https://www.renpy.org/)
2. Clone this repository:
   ```bash
   git clone <repository_url>
   ```
3. Open Ren'Py, select the project folder, and launch the game.

## 🎮 Gameplay Instructions

1. Start the game by running it through the Ren'Py launcher.
2. Choose your desired career path.
3. Navigate through career-specific scenarios.
4. Make decisions and observe their impact on your career journey.
5. Reach one of the four possible outcomes:
   - **Achieved**: Become a respected leader.
   - **Moderate**: Perform well but have room to grow.
   - **Retry**: Face setbacks but try again.

## ⚙️ Making Changes

The following files can be found in the game directory:

**script.rpy**: Located at `game/script.rpy`, this file manages scenarios, dialogues, decision branches, and game logic.

**screens.rpy**: Located at `game/screens.rpy`, this file is responsible for customizing UI elements, adjusting dialogue screens, and interactive components.

These files are essential for modifying how the story progresses and how user interactions are handled. Feel free to explore and adjust them to enhance your gaming experience.

## ➕ How to Add a New Career

You can easily add a new career using our Gradio app, which helps generate the necessary JSON files and organize assets.

### Step 1: Generate Career JSON Using Gradio

1. Run the Gradio app.
   
      👉 [JSON File Generator](https://huggingface.co/spaces/cloudyuga/JSON-file-generator-for-career-cards)

2. Enter the career details and generate the JSON file.
3. The JSON will include career scenarios, dialogues, and outcomes.

### Step 2: Add Images and Audio

1. Prepare the necessary images (`male or female career related images`, `scenario images`, `result images`) and relevant audio files for scenarios.
2. Ensure the images are of appropriate resolution for the game interface.

### Step 3: Place Files into the Game
1. Place the json file under game folder 
```bash
 game/careers/<career_category>/career_name.json
```
   - `career_category` like Healthcare, CivilServices, Education, Engineering etc.
   - `caree_name` like doctor, nurse, teacher, software_developer etc.

2. Place the images under the following directory:
    ```bash
    game/images/careers/<career_name>/
    ```
3. Place the audio files under:
    ```bash
    game/audio/<career_name>/
    ```
4. Example structure:
    ```bash
    game/careers/Healthcare/
    ├── doctor.json
    game/images/careers/doctor/
    ├── doctor.jpg
    ├── scenario1.jpg
    ├── scenario2.jpg
    ├── achieved.jpg
    ├── moderate.jpg
    ├── retry.jpg
    game/audio/doctor/
    ├── scenario1.mp3
    ├── scenario1.mp3
    ```

### Step 4: Generate Additional Audio (Optional)

- If you need more audio files, you can download them from external sources or generate them using the following script:
   ```python
      from gtts import gTTS
      text = "Welcome to Teen-Trailblazer Game. It's career related game which helps you to choose your career. So are you ready? Let's Play"
      tts = gTTS(text, lang='en')
      print("audio generated")
      tts.save("welcome.mp3")
   ```
   Save the above file as text-to-audio-generator.py and change the `text` accordingly.
- Install `gtts` package
   ```bash
      $ pip install gtts
   ```
- Run the audio generator script
   ```bash
      $ python text-to-audio-generator.py
    ```
- You can use this audio files to modify or add new audio to the game

### Step 5: Test Your Career Path

1. Launch the game and select the new career.
2. Verify the scenarios, images, and audio are displayed correctly.
---

#### 🚀 Enjoy your career adventure! 🚀

