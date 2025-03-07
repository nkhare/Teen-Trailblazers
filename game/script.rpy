# ========================
# Initialization & Styles
# ========================
define selected_career= ""
default selected_sector = ""
define healthcare_cards = []
define civil_services_cards = []
define education_cards = []
define all_career_cards = []

image score = "images/score.jpg"
#init 2 python

init python:
    
    import os, json
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
    all_career_cards = healthcare_cards + civil_services_cards + education_cards

# ========================
# Story Label
# ========================

label career_story:
    scene expression [career['CareerCard']['ImageMale']]
    "{b}{color=#FFD700}Overview:{/b} [career['CareerCard']['Overview']]{/color}"  

    $ benefits_text = "\n".join([f"- {b}" for b in career['CareerCard']['Benefits and Challenges']['Benefits']])
    "{b}{color=#00FFAA}Benefits:{/b}\n{color=#00FFAA}[benefits_text]{/color}"

    # Process Challenges in a Python block
    $ challenges_text = "\n".join([f"- {c}" for c in career['CareerCard']['Benefits and Challenges']['Job Challenges']])
    "{b}{color=#FF4500}Challenges:{/b}\n{color=#FF4500}[challenges_text]{/color}"

    $ score = 0  # Initialize score
    $ scenario_count = len(career['Scenarios'])  # Get scenario count dynamically
    $ scenario_index = 0  # Start with the first scenario

    jump scenario_loop

label scenario_loop1:
    if scenario_index >= scenario_count:
        jump game_end  

    # Set dynamic background
    scene expression career['Scenarios'][scenario_index]['BackgroundImage']
    # Display scenario details
    "{b}{color=#FFD700}[career['Scenarios'][scenario_index]['Title']]{/b}"
    scene expression career['Scenarios'][scenario_index]['BackgroundImage'] 
    "{b}{color=#FFD700}Scenario [scenario_index+1]:{/b} [career['Scenarios'][scenario_index]['Description']]{/color}"

    menu:
        "{color=#00FFAA}Option A:{/color}\n{color=#ffffff}[career['Scenarios'][scenario_index]['DecisionCards'][0]['Option']]{/color}":
            $ score += career['Scenarios'][scenario_index]['DecisionCards'][0]['Outcomes']['PersonalImpact'] + career['Scenarios'][scenario_index]['DecisionCards'][0]['Outcomes']['CommunityImpact']
            "{b}{color=#FFA500}Your decision has been made... consequences will follow.{/color}{/b}"

        "{color=#00FFAA}Option B:{/color}\n{color=#ffffff}[career['Scenarios'][scenario_index]['DecisionCards'][1]['Option']]{/color}":
            $ score += career['Scenarios'][scenario_index]['DecisionCards'][1]['Outcomes']['PersonalImpact'] + career['Scenarios'][scenario_index]['DecisionCards'][1]['Outcomes']['CommunityImpact']
            "{b}{color=#FFA500}You chose a different path... let's see where it leads.{/color}{/b}"

    # If this was the last scenario, go directly to the end
    if scenario_index == scenario_count - 1:
        jump game_end

    # Otherwise, show score and continue
    "{b}{color=#ffffff}Your current impact score so far is [score].{/color}{/b}"  # Light Blue

    menu:
        "{color=#ffa500}\nGo Back to Home\n{/color}":
            return  

        "{color=#00ff00}\nProceed to Next Scenario\n{/color}":
            $ scenario_index += 1  
            jump scenario_loop  

label game_end1:
    scene score
    "{b}{color=#ffffff} Your Final Impact Score is [score]{/color}{/b}"
    if score >= 12:
        scene expression [career['Result']['AchievedImage']]
        "{b}{color=#FFD700}[career['Result']['Achieved']]{/b}"
    elif score >= 8:
        scene expression [career['Result']['ModerateImage']]
        "{b}{color=#FFD700}[career['Result']['Moderate']]{/b}"
    else:
        scene expression [career['Result']['RetryImage']]
        "{b}{color=#FF4500}[career['Result']['Retry']]{/b}"
    
    scene expression [career['Result']['QuitImage']]
    "{b}{color=#FFD700}[career['Result']['Quit']]{/b}"  # Gold text
    return    


label careers_story:
    $ personal_growth = 50  # Personal development score
    $ community_trust = 50  # Public trust score

    scene expression career['CareerCard']['ImageMale']

    "{b}{color=#FFD700}Overview:{/b} {color=#FFFFFF}[career['CareerCard']['Overview']]{/color}"

    $ benefits_text = "\n".join([f"- {b}" for b in career['CareerCard']['Benefits and Challenges']['Benefits']])
    "{b}{color=#00FFAA}Benefits:{/b}\n{color=#00FFAA}[benefits_text]{/color}"

    # Process Challenges in a Python block
    $ challenges_text = "\n".join([f"- {c}" for c in career['CareerCard']['Benefits and Challenges']['Job Challenges']])
    "{b}{color=#FF4500}Challenges:{/b}\n{color=#FF4500}[challenges_text]{/color}"

    menu:
        "{color=#00FFAA}[career['CareerCard']['Choices'][0]['Option']]{/color}":
            $ personal_growth += career['CareerCard']['Choices'][0]['PersonalImpact']
            $ community_trust += career['CareerCard']['Choices'][0]['CommunityImpact']
            "{b}{color=#FFA500}[career['CareerCard']['Choices'][0]['Result']]{/color}{/b}"

        "{color=#00FFAA}[career['CareerCard']['Choices'][1]['Option']]{/color}":
            $ personal_growth += career['CareerCard']['Choices'][1]['PersonalImpact']
            $ community_trust += career['CareerCard']['Choices'][1]['CommunityImpact']
            "{b}{color=#FFA500}[career['CareerCard']['Choices'][1]['Result']]{/color}{/b}"

    $ scenario_index = 0  # Start with the first scenario
    $ scenario_count = len(career['Scenarios'])  # Get scenario count dynamically
    jump scenario_loop

label scenario_loop:
    if scenario_index >= scenario_count:
        jump game_end  

    scene expression career['Scenarios'][scenario_index]['BackgroundImage']
    "{b}{color=#FFD700}[career['Scenarios'][scenario_index]['Title']]{/b}"
    "{b}{color=#FFD700}Scenario [scenario_index+1]:{/b} [career['Scenarios'][scenario_index]['Description']]{/color}"

    menu:
        "{color=#00FFAA}Option A:{/color}\n{color=#ffffff}[career['Scenarios'][scenario_index]['DecisionCards'][0]['Option']]{/color}":
            $ personal_growth += career['Scenarios'][scenario_index]['DecisionCards'][0]['Outcomes']['PersonalImpact']
            $ community_trust += career['Scenarios'][scenario_index]['DecisionCards'][0]['Outcomes']['CommunityImpact']
            "{b}{color=#FFA500}Your decision has been made... consequences will follow.{/color}{/b}"

        "{color=#00FFAA}Option B:{/color}\n{color=#ffffff}[career['Scenarios'][scenario_index]['DecisionCards'][1]['Option']]{/color}":
            $ personal_growth += career['Scenarios'][scenario_index]['DecisionCards'][1]['Outcomes']['PersonalImpact']
            $ community_trust += career['Scenarios'][scenario_index]['DecisionCards'][1]['Outcomes']['CommunityImpact']
            "{b}{color=#FFA500}You chose a different path... let's see where it leads.{/color}{/b}"

    
    # If this was the last scenario, go directly to the end
    if scenario_index == scenario_count - 1:
        jump game_end

    "{b}{color=#ffffff}Your current impact score: Personal Growth = [personal_growth], Community Trust = [community_trust].{/color}{/b}"
    
    menu:
        "{color=#ffa500}\nGo Back to Home\n{/color}":
            return  
        
        "{color=#00ff00}\nProceed to Next Scenario\n{/color}":
            $ scenario_index += 1  
            jump scenario_loop  

label game_end:
    scene score
    "{b}{color=#ffffff} Your Final Impact Scores: Personal Growth = [personal_growth], Community Trust = [community_trust]{/color}{/b}"
    if personal_growth >= 70 and community_trust >= 60:
        scene expression career['Result']['AchievedImage']
        "{b}{color=#FFD700}[career['Result']['Achieved']]{/b}"
    elif personal_growth >= 70:
        scene expression career['Result']['ModerateImage']
        "{b}{color=#FFD700}[career['Result']['Moderate']]{/b}"
    else:
        scene expression career['Result']['RetryImage']
        "{b}{color=#FF4500}[career['Result']['Retry']]{/b}"
    
    return
