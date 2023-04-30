# Welcomes the user
# Gives the user options
import easygui
choices = easygui.buttonbox("Choose an option from below: ", "Welcome",
                            choices=["Add Combo", "Change Combo",
                                     "Delete Combo", "Output All Combos",
                                     "Exit"])
if choices == "Add Combo":
    easygui.msgbox("Add Combo action succeeded", "Add Combo")

elif choices == "Change Combo":
    easygui.msgbox("Change Combo action succeeded", "Change Combo")

elif choices == "Delete Combo":
    easygui.msgbox("Delete Combo action succeeded", "Delete Combo")

elif choices == "Output All Combos":
    easygui.msgbox("Output All Combos action succeeded", "Output All Combos")

elif choices == "Exit":
    print()
