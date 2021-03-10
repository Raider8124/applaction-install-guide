count = 0
while count < 5:
    answer = input("Are you looking for commonly used software? << ")

    if answer == "yes":
        anwser = input("What Distro are you using? << ")
        if anwser == "arch":
            anwser = input("What software are you looking for? Type 'list' to display all options << ")  
            if anwser == "gimp":
                print("sudo pacman -S gimp")
                print("----------------------")
            elif anwser == "blender":
                print("sudo pacman -S blender")
                print("----------------------")
            elif anwser == "git":
                print("sudo pacman -S git")
                print("----------------------")
            elif anwser == "yay":
                print("pacman -S --needed git base-devel")
                print("git clone https://aur.archlinux.org/yay.git")
                print("cd yay")
                print("makepkg -si")
                print("----------------------")
            elif anwser == "gtop":
                print("sudo pacman -S gtop  ")
                print("----------------------")
            elif anwser == "gparted":
                print("sudo pacman -S gparted")
                print("----------------------")
            elif anwser == "alarcitty":
                print("sudo pacman -S alacritty")
                print("----------------------")
            elif anwser == "i3":
                print("sudo pacman -S i3 feh dmenu rofi")
                print("---------------------------------")
            elif anwser == "nautilus":
                print("sudo pacman -S nautilus")
                print("------------------------")
            elif anwser == "thunderbird":
                print("sudo pacman -S thunderbird")
                print("----------------------------")
            elif anwser == "neovim":
                print("sudo pacman -S neovim")
                print("------------------------")
            elif anwser == "discord":
                print("sudo pacman -S discord dunst")
                print("-----------------------------")
            elif anwser == "xchat":
                print("yay -S xchat")
                print("----------------------")
            elif anwser == "openvpn":
                print("sudo pacman -S openvpn")
                print("------------------------")
            elif anwser == "steam":
                print("sudo pacman -S steam")
                print("----------------------")
            elif anwser == "minecraft":
                print("yay -S minecraft-launcher")
                print("---------------------------")
            elif anwser == "wine":
                print("yay -S wine")
                print("----------------------")
            elif anwser == "lutris":
                print("yay -S lutris")
                print("----------------------")
            elif anwser == "list":
                print("Photo Editing - gimp << ")
                print("3D Modeling - blender << ")
                print("Utililty - git - yay - gtop - gparted << ")
                print("Termnial Emulator - alacritty <<")
                print("File Manager - nautilus << ")
                print("Window Manager - i3 << ")
                print("Email Client - thunderbird << ")
                print("Text Editor - neovim << ")
                print("Social Media - discord - xchat << ")
                print("Games - steam - minecraft - wine - lutris << ")
                print("Virtual Private Network - openvpn << ")
                print("----------------------")
            else:
                print("Failed to Find application. Please rerun the app and try again. Type 'list' to display all options")
                exit()
        elif anwser == "debian":
            anwser = input("What software are you looking for? Type 'list' to display all options << ")
            if anwser == "gimp":
                print("sudo apt install gimp")
                print("----------------------")
            elif anwser == "git":
                print("sudo apt install git")
                print("----------------------")
            elif anwser == "neovim":
                print("sudo apt install neovim")
                print("----------------------")
            elif anwser == "gtop":
                print("sudo apt install gtop")
                print("----------------------")
            elif anwser == "alacritty":
                print("sudo apt install alacritty")
                print("----------------------")
            elif anwser == "i3":
                print("sudo apt install i3")
                print("----------------------")
            elif anwser == "gparted":
                print("sudo apt install gparted")
                print("----------------------")
            elif anwser == "nautilus":
                print("sudo apt install nautilus")
                print("----------------------")
            elif anwser == "xchat":
                print("sudo apt install xchat")
                print("----------------------")
            elif anwser == "discord":
                print("sudo apt install discord")
                print("----------------------")
            elif anwser == "thunderbird":
                print("sudo apt isntall thunderbird")
                print("----------------------")
            elif anwser == "blender":
                print("sudo apt install blender")
                print("----------------------")
            elif answer == "steam":
                print("sudo apt install steam")
                print("----------------------")
            elif anwser == "list":
                print("Photo Editing - gimp << ")
                print("3D Modeling - blender << ")
                print("Utililty - git - gtop - gparted << ")
                print("Termnial Emulator - alacritty <<")
                print("File Manager - nautilus << ")
                print("Window Manager - i3 << ")
                print("Email Client - thunderbird << ")
                print("Text Editor - neovim << ")
                print("Social Media - discord - xchat << ")
                print("Games - steam - wine - lutris << ")
                print("Virtual Private Network - openvpn << ")
                print("----------------------")
            else:
                print("Failed to Find application. Please rerun the app and try again. Type 'list' to display all options")
                exit()
        elif anwser == "ubuntu":
            print("This app is a work in progress and currently this app does not have any install guides for Ubuntu")

    else:
        print("Ok Bye")
        exit()
