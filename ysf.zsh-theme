# ysftheme
# Main theme from https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/essembeh.zsh-theme
# a little colorful than main theme

# git plugin 
ZSH_THEME_GIT_PROMPT_PREFIX="%{$FG[129]%}git:(%{$reset_color%}%{$fg[red]%}"
ZSH_THEME_GIT_PROMPT_SUFFIX="%{$reset_color%}%{$FG[129]%})%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_DIRTY="%{$fg[blue]%}) %{$fg[yellow]%}✗%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_CLEAN="%{$fg[blue]%})"

function zsh_gitstatus {
	ref=$(git symbolic-ref HEAD 2> /dev/null) || return
	GIT_STATUS=$(git_prompt_status)
	if [[ -n $GIT_STATUS ]]; then
		GIT_STATUS=" $GIT_STATUS"
	fi
	echo "$ZSH_THEME_GIT_PROMPT_PREFIX${ref#refs/heads/}$GIT_STATUS$ZSH_THEME_GIT_PROMPT_SUFFIX"
}

# for color codes "spectrum_ls"
local ZSH_USER_COLOR="084"
local ZSH_CENTER_COLOR="085"
local ZSH_HOSTNAME_COLOR="086"
local ZSH_PREFIX=""s

if [[ -n "$SSH_CONNECTION" ]]; then
	# display the source address if connected via ssh
	ZSH_PREFIX="%{$fg[yellow]%}[$(echo $SSH_CONNECTION | awk '{print $1}')]%{$reset_color%} "
	# use orange color to highlight a remote connection
	ZSH_USER_COLOR="166" #orange
elif [[ -r /.dockerenv ]]; then
	# also prefix prompt inside a docker contrainer
	ZSH_PREFIX="%{$fg[yellow]%}[docker]%{$reset_color%} "
fi

if [[ $UID = 0 ]]; then
	# always use red & pink for root sessions, even in ssh
	ZSH_USER_COLOR="196" # red
	ZSH_CENTER_COLOR="198" # pink
	ZSH_HOSTNAME_COLOR="205" # pink
fi

# main prompt
PROMPT='${ZSH_PREFIX}%{$FG[$ZSH_USER_COLOR]%}%n%{$reset_color%}%{$FG[$ZSH_CENTER_COLOR]%}@%{$reset_color%}%{$FG[$ZSH_HOSTNAME_COLOR]%}%M%{$reset_color%}:%{%B$FG[228]%}%~%{$reset_color%} $(zsh_gitstatus)%(!.#.>) '