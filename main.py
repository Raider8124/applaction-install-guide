answer = input("Are you looking for commonly used software << ")

if answer == "yes":
    anwser = input("What software are you looking for? Type 'list' to display all options << ")  
    if anwser == "gimp":
        print("sudo pacman -S gimp")
    elif anwser == "blender":
        print("sudo pacman -S blender")
    elif anwser == "git":
        print("sudo pacman -S git")
    elif anwser == "i3":
        print("sudo pacman -S i3 feh dmenu rofi")
    elif anwser == "nautilus":
        print("sudo pacman -S nautilus")
    elif anwser == "thunderbird":
        print("sudo pacman -S thunderbird")
    elif anwser == "neovim":
        print("sudo pacman -S neovim")
    elif anwser == "discord":
        print("sudo pacman -S discord dunst")
    elif anwser == "openvpn":
        print("sudo pacman -S openvpn")
    elif anwser == "list":
        print("Photo Editing - gimp << ")
        print("3D Modeling - blender << ")
        print("Utililty - git << ")
        print("File Manager - nautilus << ")
        print("Window Manager - i3 << ")
        print("Email Client - thunderbird << ")
        print("Text Editor - neovim << ")
        print("Social Media - discord << ")
        print("Virtual Private Network - openvpn << ")
else:
    print("Ok Bye")
    exit()

