#!/bin/bash

# Step 1: Install Oh My Zsh
echo "Step 1: Installing Oh My Zsh..."
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Step 2: Install Plugins
echo "Step 2: Installing Zsh Plugins..."
ZSH_CUSTOM=${ZSH_CUSTOM:-~/.oh-my-zsh/custom}
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-autosuggestions.git $ZSH_CUSTOM/plugins/zsh-autosuggestions

# Step 3: Install Custom Themes
echo "Step 3: Installing Custom Zsh Themes..."
THEME_DIR=$ZSH_CUSTOM/themes
mkdir -p $THEME_DIR/zsh-syntax-highlighting
rm $THEME_DIR/ysf.zsh-theme
rm $THEME_DIR/zsh-syntax-highlighting/catppuccin_mocha-zsh-syntax-highlighting.zsh
wget -P $THEME_DIR/zsh-syntax-highlighting https://github.com/catppuccin/zsh-syntax-highlighting/raw/main/themes/catppuccin_mocha-zsh-syntax-highlighting.zsh
wget -P $THEME_DIR https://github.com/ysfsvm/dotfiles/raw/main/zsh/ysf.zsh-theme

# Step 4: Apply Custom .zshrc
echo "Step 4: Applying Custom .zshrc..."
rm $HOME/.zshrc
wget -P $HOME https://github.com/ysfsvm/dotfiles/raw/main/zsh/.zshrc

# Done!
echo "Setup completed! Please restart your terminal to see the changes."

