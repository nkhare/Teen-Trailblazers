# Teen-Trailblazer - A Ren'Py Visual Novel

Welcome to the **Career Card Game**! This interactive visual novel, built using **Ren'Py**, offers an engaging experience where players navigate through different career paths, face real-world scenarios, and make decisions that impact their journey.

## 🚀 Features

- Choose from multiple career options like **Doctor**, **Civil Engineer**, **Firefighter**, and **School Administrator**.
- Experience dynamic scenarios and face decision-making challenges.
- Track your progress through success, moderate performance, failure, or game-over outcomes.
- Immersive visuals and animations.

## 🛠️ Requirements

- Ren'Py SDK (version 8.3.4 or later)
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
   - **Game Over**: Experience career failure.

## ➕ How to Add a New Career

You can easily add a new career using our Gradio app, which helps generate the necessary JSON files and organize assets.

### Step 1: Generate Career JSON Using Gradio

1. Run the Gradio app by executing:
   ```bash
   python json_file_generator.py
   ```
2. Enter the career details and generate the JSON file.
3. The JSON will include career scenarios, dialogues, and outcomes.

### Step 2: Add Images and Audio

1. Prepare the necessary images (`achieved.jpg`, `moderate.jpg`, `retry.jpg`, `game_over.jpg`) and any relevant audio files.
2. Ensure the images are of appropriate resolution for the game interface.

### Step 3: Place Files into the Game

1. Place the images under the following directory:
    ```bash
    game/images/careers/<career_name>/
    ```
2. Place the audio files under:
    ```bash
    game/audio/<career_name>/
    ```
3. Example structure:
    ```bash
    game/career/doctor/
    ├── doctor.json
    game/images/careers/doctor/
    ├── achieved.jpg
    ├── moderate.jpg
    ├── retry.jpg
    ├── game_over.jpg
    game/audio/doctor/
    ├── scenario1.mp3
    ```

### Step 4: Generate Additional Audio (Optional)

- If you need more audio files, you can download them from external sources or generate them using the following script:
    ```bash
    python text-to-audio-generator.py
    ```

### Step 5: Additional Changes

- If further adjustments are needed for a new career, refer to `script.rpy` and `screens.rpy` for scenario-specific configurations and dialogue management.

### Step 6: Test Your Career Path

1. Launch the game and select the new career.
2. Verify the scenarios, images, and audio are displayed correctly.

## 🖼️ Images and Graphics

Ensure the following image assets are placed in the `/game/images` directory:

- **arrow\_idle.png** and **arrow\_hover.png** for navigation.
- Scenario-specific images for different careers.

## 🛡️ Troubleshooting

- If the game doesn't load properly, check for missing images or incorrect paths in `screens.rpy`.
- For Git-related issues, ensure your changes are committed before pulling.
  ```bash
  git add .
  git commit -m "Your commit message"
  git pull origin main --rebase
  ```
- If merge conflicts occur, resolve them and continue the rebase using:
  ```bash
  git rebase --continue
  ```

## 🤝 Contributing

We welcome contributions! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/new-feature`.
3. Commit your changes: `git commit -m 'Add new feature'`.
4. Push to your branch: `git push origin feature/new-feature`.
5. Create a Pull Request.

## 📜 License

This project is licensed under the MIT License. See `LICENSE` for details.

---
Enjoy your career adventure! 🚀

