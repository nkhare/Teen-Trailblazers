# ========================
# Initialization & Styles
# ========================
define selected_career= ""
default selected_sector = ""
define healthcare_cards = []
define civil_services_cards = []
define education_cards = []
define all_career_cards = []
define user_name = ""
default user_gender = ""
define user = Character(name="user_name", dynamic = True)

image score = "images/score.jpg"
image feedback = "images/feedback.jpg"

init python:
    import os, json, random
    def load_career_cards(sector):
        # Construct the folder path. This assumes your JSON files are in game/careers/<sector>/
        folder = os.path.join(config.basedir, "game", "careers", sector)
        cards = []
        if os.path.isdir(folder):
            for filename in os.listdir(folder):
                renpy.log("Found file: " + filename)
                if filename.endswith(".json"):
                    path = os.path.join(folder, filename)
                    try:
                        with open(path, "r", encoding="utf-8") as f:
                            data = json.load(f)
                        cards.append(data)
                        renpy.log("Loaded card from: " + path)
                    except Exception as e:
                        renpy.log("Error loading {}: {}".format(path, e))
        else:
            renpy.log("Folder not found: " + folder)
        return cards
    # Load JSON data for each sector.
    healthcare_cards = load_career_cards("Healthcare")
    civil_services_cards = load_career_cards("CivilServices")
    education_cards = load_career_cards("Education")
    engineering_cards = load_career_cards("Engineering")
    all_career_cards = healthcare_cards + civil_services_cards + education_cards + engineering_cards

    def get_random_career():
        enabled = [card for card in all_career_cards if card["CareerCard"]["Enabled"] == 1]
        return random.choice(enabled)

# ========================
# Story Labels
# ========================

label start:
    scene black
    play music "audio/background_music.mp3" loop  # Play music on loop.
    jump random_selection

label random_selection:
    call screen job_selection_menu
    $ career = _return
    #"You have been assigned the career: [career['CareerCard']['Title']]."
    jump careers_story

label careers_story:
    $ personal_growth = 20  # Personal development score
    $ community_trust = 20  # Public trust score
    $ secured_score = personal_growth + community_trust
    
    scene expression career['CareerCard']['ImageMale']
    "Welcome on-duty [career['CareerCard']['Title']] {color=#ffa500}{b}[user]!{/b}{/color}" 
    "{b}{color=#FFD700}Overview:{/b}\n\n{color=#FFFFFF}{size=25}\"[career['CareerCard']['Overview']]\"{/color}{/size}"

    $ benefits_text = "\n".join([f"- {b}" for b in career['CareerCard']['Benefits and Challenges']['Benefits']])
    "{color=#00FF00}Benefits:\n{size=25}{color=#ffffff}[benefits_text]{/color}{/size}"

    # Process Challenges in a Python block
    $ challenges_text = "\n".join([f"- {c}" for c in career['CareerCard']['Benefits and Challenges']['Job Challenges']])
    "{color=#ff0000}Challenges:\n{size=25}{color=#ffffff}[challenges_text]{/color}{/size}"

    menu:
        "How Will You Step Into This Role [user]??? {color=#ffff00}Choose one of the above options{/color}"

        #"{color=#00FFAA}[career['CareerCard']['Choices'][0]['Option']]{/color}":
        "{color=#00FFAA}Option A:{/color}\n{color=#ffffff}[career['CareerCard']['Choices'][0]['Option']]{/color}":
            $ personal_growth += career['CareerCard']['Choices'][0]['PersonalImpact']
            $ community_trust += career['CareerCard']['Choices'][0]['CommunityImpact']
            "{color=#FFA500}{size=25}[career['CareerCard']['Choices'][0]['Result']]{/size}{/color}"

        #"{color=#00FFAA}[career['CareerCard']['Choices'][1]['Option']]{/color}":
        "{color=#00FFAA}Option B:{/color}\n{color=#ffffff}[career['CareerCard']['Choices'][1]['Option']]{/color}":
            $ personal_growth += career['CareerCard']['Choices'][1]['PersonalImpact']
            $ community_trust += career['CareerCard']['Choices'][1]['CommunityImpact']
            "{color=#ffffff}{size=25}[career['CareerCard']['Choices'][1]['Result']]{/size}{/color}"


    $ scenario_index = 0  # Start with the first scenario
    $ scenario_count = len(career['Scenarios'])  # Get scenario count dynamically
    
    jump scenario_loop

label scenario_loop:
    if scenario_index >= scenario_count:
        jump game_end  

    scene expression career['Scenarios'][scenario_index]['BackgroundImage']
    "{color=#FFD700}[career['Scenarios'][scenario_index]['Title']]:{/color}{color=#ffffff} [career['Scenarios'][scenario_index]['Description']]{/color}"

    menu:
        "Your decision will shape your journey in this career.{color=#ffff00}{b} Choose wisely!{/b}{/color}"
        "{color=#00FFAA}Option A:{/color}\n{color=#ffffff}[career['Scenarios'][scenario_index]['DecisionCards'][0]['Option']]{/color}":
            $ personal_growth += career['Scenarios'][scenario_index]['DecisionCards'][0]['Outcomes']['PersonalImpact']
            $ community_trust += career['Scenarios'][scenario_index]['DecisionCards'][0]['Outcomes']['CommunityImpact']
            $ secured_score = personal_growth + community_trust
            "{b}{color=#FFA500}[career['CareerCard']['Title']] [user], your decision is set in motion… let’s see what comes next.{/color}{/b}"

        "{color=#00FFAA}Option B:{/color}\n{color=#ffffff}[career['Scenarios'][scenario_index]['DecisionCards'][1]['Option']]{/color}":
            $ personal_growth += career['Scenarios'][scenario_index]['DecisionCards'][1]['Outcomes']['PersonalImpact']
            $ community_trust += career['Scenarios'][scenario_index]['DecisionCards'][1]['Outcomes']['CommunityImpact']
            $ secured_score = personal_growth + community_trust
            "{b}{color=#FFA500}[career['CareerCard']['Title']] [user], You chose a different path... let's see where it leads.{/color}{/b}"

    
    # If this was the last scenario, go directly to the end
    if scenario_index == scenario_count - 1:
        jump game_end

    #"{b}{color=#ffffff}Your current impact score: Personal Growth = [personal_growth], Community Trust = [community_trust].{/color}{/b}"
    "{b}{color=#ffff00}Your current impact score is:[secured_score]{/color}{/b}"
      
    menu:
        "{color=#ffa500}\nGo back to play again\n{/color}":
            return
            #call screen navigation  

        "{color=#ffffff}\nProvide Your Feedback\n{/color}":
            jump feedback

        "{color=#00ff00}\nContinue your mission\n{/color}":
            $ scenario_index += 1  
            jump scenario_loop  

        "{color=#ff0000}\nQuit\n{/color}":
            $ renpy.quit()


label game_end:
    scene score
    "{b}{color=#ff0000} [career['CareerCard']['Title']] [user], Your Final Impact Score is:[secured_score]{/color}{/b}"

    if secured_score >= 70:
        scene expression career['Result']['AchievedImage']
        "{b}{color=#FFD700}[career['Result']['Achieved']]{/b}"

    elif secured_score >= 60:
        scene expression career['Result']['ModerateImage']
        "{b}{color=#FFD700}[career['Result']['Moderate']]{/b}"

    else:
        scene expression career['Result']['RetryImage']
        "{b}{color=#FF4500}[career['Result']['Retry']]{/b}"
    
    scene expression career['Result']['QuitImage']
    "{b}{color=#ff00ff}Game Over!{/b}"

    jump feedback
    
label feedback:
    scene feedback
    "Thank you for playing! Please provide your feedback."
    scene black
    call screen feedback_screen
    "Thank you for your feedback!"
    return