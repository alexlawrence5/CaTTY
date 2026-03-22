#!/bin/bash
sudo pacman -Syu dialog
HEIGHT=15
WIDTH=40
CHOICE_HEIGHT=4
BACKTITLE="CaTTY 0.2"
TITLE="CaTTY Installation Menu"
MENU="Choose one of the following options:"

OPTIONS=(
1 "Install Cava"
2 "Install Cmatrix"
3 "Install Fastfetch"
4 "Install TTY-Clock"
5 "ALl-In-One"
6 "Quit"
)

CHOICE=$(dialog --clear \
                --backtitle "$BACKTITLE" \
                --title "$TITLE" \
                --menu "$MENU" \
                $HEIGHT $WIDTH $CHOICE_HEIGHT \
                "${OPTIONS[@]}" \
                2>&1 >/dev/tty)

clear
case $CHOICE in
    1)
        echo "Installing cava..."
        sudo bash cava/Installer
        ;;
    2)
        echo "Installing cmatrix..."
        sudo bash cmatrix/Installer
        ;;
    3)
        echo "Installing Fastfetch..."
        sudo bash fastfetch/Installer
        ;;
    4)
        echo "Install TTY-Clock..."
        sudo bash ttyclock/Installer
        ;;
    5)
        sudo bash cava/Installer
        sudo bash cmatrix/Installer
        sudo bash fastfetch/Installer
        sudo bash ttyclock/Installer
        ;;
    6)
        exit 0
esac

# did i forgot something?
