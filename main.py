count = 0
while count < 5:
    answer = input("Are you looking for commonly used software? << ")

    if answer == "yes":
        anwser = input("What Distro are you using? << ")
        if anwser == "arch":
            anwser = input("What software are you looking for? Type 'list' to display all options << ")  
            if anwser == "gimp":
                print("sudo pacman -S gimp")
            elif anwser == "blender":
                print("sudo pacman -S blender")
            elif anwser == "git":
                print("sudo pacman -S git")
            elif anwser == "yay":
                print("pacman -S --needed git base-devel")
                print("git clone https://aur.archlinux.org/yay.git")
                print("cd yay")
                print("makepkg -si")
            elif anwser == "gtop":
                print("sudo pacman -S gtop  ")
            elif anwser == "gparted":
                print("sudo pacman -S gparted")
            elif anwser == "alarcitty":
                print("sudo pacman -S alacritty")
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
            elif anwser == "xchat":
                print("yay -S xchat")
            elif anwser == "openvpn":
                print("sudo pacman -S openvpn")
            elif anwser == "steam":
                print("sudo pacman -S steam")
            elif anwser == "minecraft":
                print("yay -S minecraft-launcher")
            elif anwser == "wine":
                print("yay -S wine")
            elif anwser == "lutris":
                print("yay -S lutris")
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
            else:
                print("Failed to Find application. Please rerun the app and try again. Type 'list' to display all options")
                exit()
        elif anwser == "debian":
            anwser = input("What software are you looking for? Type 'list' to display all options << ")
            if anwser == "gimp":
                print("sudo apt install gimp")
            elif anwser == "git":
                print("sudo apt install git")
            elif anwser == "neovim":
                print("sudo apt install neovim")
            elif anwser == "gtop":
                print("sudo apt install gtop")
            elif anwser == "alacritty":
                print("sudo apt install alacritty")
            elif anwser == "i3":
                print("sudo apt install i3")
            elif anwser == "gparted":
                print("sudo apt install gparted")
            elif anwser == "nautilus":
                print("sudo apt install nautilus")
            elif anwser == "xchat":
                print("sudo apt install xchat")
            elif anwser == "discord":
                print("sudo apt install discord")
            elif anwser == "thunderbird":
                print("sudo apt isntall thunderbird")
            elif anwser == "blender":
                print("sudo apt install blender")
            elif answer == "steam":
                print("sudo apt install steam")
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
            else:
                print("Failed to Find application. Please rerun the app and try again. Type 'list' to display all options")
                exit()
        elif anwser == "ubuntu":
            print("This app is a work in progress and currently this app does not have any install guides for Ubuntu")

    else:
        print("Ok Bye")
        exit()
