# Set the directory we want to store zinit and plugins
ZINIT_HOME="${XDG_DATA_HOME:-${HOME}/.local/share}/zinit/zinit.git"

# Download Zinit, if it's not there yet
if [ ! -d "$ZINIT_HOME" ]; then
   mkdir -p "$(dirname $ZINIT_HOME)"
   git clone https://github.com/zdharma-continuum/zinit.git "$ZINIT_HOME"
fi

# Source/Load zinit
source "${ZINIT_HOME}/zinit.zsh"

# Add in zsh plugins
zinit light zsh-users/zsh-syntax-highlighting
zinit light zsh-users/zsh-completions
zinit light zsh-users/zsh-autosuggestions
zinit light Aloxaf/fzf-tab

# Nix Shell ZSH Shim
zinit light chisui/zsh-nix-shell
export NIX_BUILD_SHELL="zsh"

# Add in snippets
zinit snippet OMZP::git
zinit snippet OMZP::sudo
zinit snippet OMZP::kubectl
zinit snippet OMZP::kubectx
zinit snippet OMZP::command-not-found

# Load completions
autoload -Uz compinit && compinit

zinit cdreplay -q

# Initialize oh-my-posh
eval "$(oh-my-posh init zsh --config $HOME/.config/omp/config.yaml)"

# History Settings
HIST_STAMPS="yyyy-mm-dd"
HISTFILE=~/.zhistory
HISTSIZE=SAVEHIST=10000
HISTDUP=erase
setopt appendhistory
setopt sharehistory
setopt hist_ignore_space
setopt hist_ignore_all_dups
setopt hist_save_no_dups
setopt hist_ignore_dups
setopt hist_find_no_dups

# Completion styling
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Za-z}'
zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"
zstyle ':completion:*' menu no
zstyle ':fzf-tab:complete:cd:*' fzf-preview 'ls --color $realpath'
zstyle ':fzf-tab:complete:__zoxide_z:*' fzf-preview 'ls --color $realpath'

# Shell Integration
eval "$(fzf --zsh)"
eval "$(zoxide init --cmd cd zsh )"

# Set nvim as default editor
export EDITOR="nvim"
export VISUAL="nvim"

# Aliases and custom functions
ipinfo() {
    curl https://ipinfo.io/$1
}

unalias gcp
gcp() {
    git add . && git commit -m $1 && git push
}

compress() {
    ffmpeg -i $1 -qscale:v 2 $1-compressed.jpg    
}

alias ipinfo
alias ipa="ip -c a"
alias top="bashtop"
alias htop="bashtop"
alias cat="bat --pager=never"
alias catp="bat -pp"
alias pcat="bat -pp"
alias nano="nvim"
alias vim="nvim"
alias vi="nvim"
alias fyay="flatpak update -y && yay"

# Vms
ubuntu() {
    quickemu --vm ~/ubuntu-22.04.conf --display none
    remmina -c ~/.local/share/remmina/group_spice_linux-kvm_localhost-5930.remmina & ; disown
}
