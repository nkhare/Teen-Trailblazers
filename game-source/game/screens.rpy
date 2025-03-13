################################################################################
## Initialization
################################################################################

init offset = -1

######### renpy loading screen #####
#screen loading():
 #   zorder 200
  #  add "images/careers.jpg"  # Ensure the image exists in game/images
   # text "Loading, please wait..." at truecenter

## Navigation screen ###########################################################
##
## This screen is included in the main page, and provides navigation
## to other menus, and to start the game.
# ✅ Define Global Variable for Gender Selection

screen navigation():
    modal True
    tag menu

    # Background with a gradient (dark professional theme)
    frame:
        style "random_job_selection_frame"
        xysize (1200, 800)
        background "#000000"  # Same Dark Background
        padding (30, 30, 30, 30)
        align (0.5, 0.5)

        vbox:
            spacing 60
            xalign 0.5
            yalign 0.5

            # ✅ Heading Text
            text "📝 Create Your Player Profile" size 50 color "#ffd700" xalign 0.5 bold True
            text "👉 Fill in your details to start your career journey." size 28 color "#ffffff" xalign 0.5

            # ✅ Name Input Field (with glowing effect)
            vbox:
                spacing 20
                xalign 0.5
                text "Enter Your Name:" size 40 color "#ffffff" xalign 0.5
                input value VariableInputValue("user_name") length 20 color "#00ff00" at input_glow_effect xalign 0.5 

            # ✅ Select Gender
            vbox:
                spacing 20
                xalign 0.5
                text "Select Your Gender:" size 40 color "#ffffff" xalign 0.5

                hbox:
                    spacing 80
                    xalign 0.5

                    # ✅ Male Button (Green Border When Selected)
                    frame:
                        background Frame(Solid("#0000ff" if user_gender == "Male" else "#000000"), 10, 10)
                        padding (5, 5)
                        imagebutton:
                            idle "images/male_icon.png"
                            hover "images/male_icon.png"
                            action [
                                SetVariable("user_gender", "Male"),
                                Function(renpy.restart_interaction)
                            ]
                            at image_button_size
                            tooltip "Select Male"

                    # ✅ Female Button (Pink Border When Selected)
                    frame:
                        background Frame(Solid("#ff1493" if user_gender == "Female" else "#000000"), 10, 10)
                        padding (5, 5)
                        imagebutton:
                            idle "images/female_icon.png"
                            hover "images/female_icon.png"
                            action [
                                SetVariable("user_gender", "Female"),
                                Function(renpy.restart_interaction)
                            ]
                            at image_button_size
                            tooltip "Select Female"

            # ✅ Continue Button (with cool glow and shake effect)
            hbox:
                spacing 300
                xalign 0.5
                yalign 0.9
                textbutton "✅ Continue" action Show("game_mode_selection") style "my_textbutton"

# =========== 🌟 Animations and Effects ===================

# ✅ Input Field Glow Effect
transform input_glow_effect:
    on idle:
        parallel:
            linear 0.4 matrixcolor TintMatrix("#00ff00")
            linear 0.4 matrixcolor TintMatrix("#ffffff")
        repeat

# ✅ Button Glow Effect for Selected Gender
transform image_button_size:
    zoom 0.15

# ✅ Green Glow Effect for Male Selection
transform selected_male_effect:
    on idle:
        parallel:
            linear 0.5 matrixcolor TintMatrix("#00ff00")
            linear 0.5 matrixcolor TintMatrix("#ffffff")
        repeat

# ✅ Pink Glow Effect for Female Selection
transform selected_female_effect:
    on idle:
        parallel:
            linear 0.5 matrixcolor TintMatrix("#ff1493")
            linear 0.5 matrixcolor TintMatrix("#ffffff")
        repeat

# ✅ Continue Button Shake Effect
transform continue_button_shake:
    zoom 0.15
    parallel:
        linear 0.1 rotate 50
        linear 0.1 rotate -50
#    repeat

### ✔ **2. Game Mode Selection (Play or Manual Career)**
#This screen will allow users to either play a game or manually choose a career.

screen game_mode_selection():
    modal True
    tag menu

    # Background with a gradient
    frame:
        style "random_job_selection_frame"
        xysize (1200, 1000)
        background "#000000"  # Same Dark Background
        padding (30, 30, 30, 30)
        align (0.5, 0.5)

        vbox:
            spacing 60
            xalign 0.5
            yalign 0.5

            # 🎓 Beautiful Heading Text
             # ✅ Dynamic Welcome Message
            if user_gender == "Male":
                text "👨‍💼 Welcome Mr. [user_name]!" size 50 color "#00ff00" bold True xalign 0.5
            else:
                text "👩‍💼 Welcome Ms. [user_name]!" size 50 color "#ff00ff" bold True xalign 0.5

        
            text "🎮 How do you want to play the game?" size 50 color "#ffd700" xalign 0.5 bold True
            text "👉 Choose one of the following modes to start your career journey." size 28 color "#ffffff" xalign 0.5

            # ✅ Option 1: Play Random Career
            
            textbutton "🎲 Play Random Career" style "my_textbutton":
                action Jump("random_selection")
                xalign 0.5
               # at button_glow_effect

            # ✅ Option 2: Choose Career Manually
            
            textbutton "📖 Choose Career Manually" style "my_textbutton":
                action Show("sector_selection")
                xalign 0.5
              #  at button_glow_effect

            # ✅ Navigation Buttons
            hbox:
                spacing 300
                xalign 0.5
                yalign 0.9
                #textbutton "⬅️ Back" action Return() style "my_textbutton"
                textbutton "⬅️ Back" action Show("navigation") style "my_textbutton"
                textbutton "✅ Continue" action Return(selected_career) style "my_textbutton"

## Feedback Screen
screen feedback_screen():
    modal True
    tag menu

    frame:
        style "random_job_selection_frame"
        xysize (1200, 1000)
        background "#000000"
        padding (30, 30, 30, 30)
        align (0.5, 0.5)

        vbox:
            spacing 60
            xalign 0.5
            yalign 0.5

            text "📝 We Value Your Feedback!" size 50 color "#ffd700" bold True xalign 0.5
            text "Please click below to provide your feedback and help us improve." size 28 color "#ffffff" xalign 0.5

            textbutton "📄 Open Feedback Form" style "my_textbutton":
                action Function(renpy.open_url, "https://docs.google.com/forms/d/e/1FAIpQLSfKiG13BO0IEygurvS05cEMQwNSrosIrNaoiIFeVkS4ASKbZw/viewform?usp=pp_url")
                xalign 0.5

            textbutton "⬅️ Back" action Return() style "my_textbutton" xalign 0.5
            #textbutton "❌ Quit Game" action Quit(confirm=True) style "my_textbutton" xalign 0.5
            textbutton "❌ Quit Game" action Function(renpy.quit) style "my_textbutton" xalign 0.5

# Define a custom textbutton style to avoid using the built-in "textbutton" style.
#init python:
 #   style.my_textbutton = Style("default")    
  #  style.my_textbutton.font = "DejaVuSans.ttf" # Change this to a font available in your project.
   # style.my_textbutton.size = 20
 #   style.my_textbutton.color = "#ffffff"
  #  style.my_textbutton.background = "#444444"
   # style.my_textbutton.hover_background = "#666666"
   # style.my_textbutton.xpadding = 20
   # style.my_textbutton.ypadding = 10
init python:
    style.my_textbutton = Style("default")    
    style.my_textbutton.font = "DejaVuSans-Bold.ttf"
    style.my_textbutton.size = 20
    style.my_textbutton.color = "#ffffff"
    style.my_textbutton.background = Frame("#444444", 10, 10)  # Simulated rounded corners
    style.my_textbutton.hover_background = Frame("#ff4500", 10, 10)
    style.my_textbutton.selected_background = Frame("#ff6347", 10, 10)
    style.my_textbutton.xpadding = 20
    style.my_textbutton.ypadding = 10
    style.my_textbutton.outlines = [(2, "#000000", 0, 0)]

############# Careers screen#####################################
#screen for start navigation menu
screen job_selection_menu():
    modal True
    tag menu

    # ✅ Automatically Assign a Random Career When Screen Loads
    default selected_career = get_random_career()

    # Background with a gradient
    frame:
        style "random_job_selection_frame"
        xysize (1200, 800)
        padding (30, 30, 30, 30)
        background "#000000"  # Dark background
        align (0.5, 0.5)

        vbox:
            spacing 40
            xalign 0.5
            yalign 0.5

            # Heading Text
            text "🎓 Welcome to Career Card Game!" size 50 color "#ffd700" xalign 0.5 bold True
            text "✨ You have been randomly assigned a career!" size 32 color "#ffffff" xalign 0.5

            # ✅ Animated Wheel (Just for Effect, No Click Needed)
            image "images/wheel.png" at spin_button_effect xalign 0.5

            # ✅ Show Assigned Career
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 20

                # 💎 Text: Career Assigned
                text "🔹 Your career is:" size 40 color "#00ff00" xalign 0.5

                # ✅ Career Image
                imagebutton:
                    xalign 0.5
                    yalign 0.5
                    idle selected_career["CareerCard"]["ImageMale"]
                    hover selected_career["CareerCard"]["ImageMale"]
                    action Return(selected_career)
                    at career_pop_effect

                # ✅ Career Title
                text "[selected_career['CareerCard']['Title']]" size 45 color "#ffff00" xalign 0.5 yalign 0.5
                text "Are you interested?" size 25 color "#ffffff" xalign 0.5

            # Navigation Buttons
            hbox:
                spacing 200
                xalign 0.5
                yalign 0.9
                #textbutton "⬅️ Back" action Return() style "my_textbutton"
                textbutton "⬅️ Back" action Show("game_mode_selection") style "my_textbutton"
                textbutton "🔄 Re-Roll Career" action SetScreenVariable("selected_career", get_random_career()) style "my_textbutton"
                textbutton "✅ Continue" action Return(selected_career) style "my_textbutton"

# =========== 🌟 Animations and Effects ===================
transform spin_button_effect:
    zoom 0.1
    parallel:
        linear 0.2 rotate 90
        linear 0.2 rotate -90
    #repeat

transform career_pop_effect:
    zoom 0.05
    linear 0.2 zoom 0.15
    linear 0.1 zoom 0.12
    linear 0.1 zoom 0.15

#screen for careers navigation menu
screen sector_selection():
    modal True
    tag menu

    frame:
        style "job_selection_frame"
        align (0.5, 0.5)
        xysize (1200, 800)
        background "#000000"
        padding (30, 30, 30, 30)

        vbox:
            spacing 40
            xalign 0.5

            # Title
            # ✅ Heading Text (with a glowing effect)
            text "💼 Choose Your Career Sector" size 50 color "#ffd700" xalign 0.5 bold True
            text "👉 Select a sector to explore careers." size 28 color "#ffffff" xalign 0.5

#            text "Careers" size 50 color "#000000" xalign 0.5
            # Sector selection buttons
    
            hbox:
                spacing 50
                textbutton "Healthcare" action SetVariable("selected_sector", "Healthcare") style "my_textbutton"
                textbutton "Civil Services" action SetVariable("selected_sector", "Civil Services") style "my_textbutton"
                textbutton "Education" action SetVariable("selected_sector", "Education") style "my_textbutton"
                textbutton "Engineering" action SetVariable("selected_sector", "Engineering") style "my_textbutton"

            # If a sector is selected, display the career options for that sector.
            if selected_sector:
                # Create a dictionary mapping sectors to their career card lists.
                $ sectors = {
                    "Healthcare": healthcare_cards,
                    "Civil Services": civil_services_cards,
                    "Education": education_cards,
                    "Engineering": engineering_cards
                }
                if sectors[selected_sector]:
                    vbox:
                        spacing 30
                        text "[selected_sector] Careers" size 40 color "#ffd700" xalign 0.5
                        hbox:
                            spacing 40
                            for card in sectors[selected_sector]:
                                vbox:
                                    spacing 30
                                    imagebutton:
                                        idle card["CareerCard"]["ImageMale"]
                                        hover card["CareerCard"]["ImageMale"]
                                        action [SetVariable("career", card), Start("careers_story")]
                                        at button_resize
                                    textbutton "[card['CareerCard']['Title']]" action [SetVariable("career", card), Start("careers_story")] style "my_textbutton"
                else:
                    text "No [selected_sector] career cards available." size 30 color "#ffffff" xalign 0.5
            else:
                text "Please select a sector above." size 30 color "#000000" xalign 0.5

            # Navigation buttons
            hbox:
                spacing 500
                #textbutton "⬅️ Back" action Return() style "my_textbutton"
                textbutton "⬅️ Back" action Show("game_mode_selection") style "my_textbutton"
    

transform button_resize:
    zoom 0.15



################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)


################################################################################
## In-game screens
################################################################################
## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

#screen say(who, what):

 #   window:
  #      id "window"

   #     if who is not None:

    #        window:
     #           id "namebox"
      #          style "namebox"
       #         text who id "who"

       # text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    #if not renpy.variant("small"):
     #   add SideImage() xalign 0.0 yalign 1.0
screen say(who, what):

    # Main dialogue window
    window:
        id "window"
        style "say_window"

        # Display character name (if provided)
        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who" style "say_label"

        # Display dialogue text
        text what id "what" style "say_text"

    # Custom Next Arrow Button
    imagebutton:
        idle "arrow_idle.png"  # Arrow image when idle
        hover "arrow_hover.png"  # Arrow image on hover
        action RollForward()  # Advances dialogue
        align (0.95, 0.9)  # Position: bottom-right corner

    # Show side image (if available) for larger screens
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0
    
## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False


screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")



################################################################################
## Main and Game Menu Screens
################################################################################
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

image opening_page = "images/bg-opening-page.jpg"

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
