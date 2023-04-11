alias ll='ls -al'
alias be='envchain aws bundle exec'
alias beb='envchain aws bundle exec bricolage'
alias gaws='envchain aws aws --profile=global --region=us-east-1'
alias kubectl-stg='envchain aws kubectl --context cookpad-global-1-search-staging'
alias kubectl-pre='envchain aws kubectl --context cookpad-global-1-search-preprod'
alias kubectl-prd='envchain aws kubectl --context cookpad-global-1-search-prod'

# terminal
export PROMPT='%F{240}%1~%f %# '
export CLICOLOR=1

# auto completion
autoload -Uz compinit && compinit

# history
setopt EXTENDED_HISTORY
SAVEHIST=10000
HISTSIZE=5000
setopt APPEND_HISTORY
setopt INC_APPEND_HISTORY
setopt HIST_EXPIRE_DUPS_FIRST 
setopt HIST_IGNORE_DUPS
setopt HIST_FIND_NO_DUPS
setopt HIST_REDUCE_BLANKS

# git
autoload -Uz vcs_info
precmd_vcs_info() { vcs_info }
precmd_functions+=( precmd_vcs_info )
setopt prompt_subst
RPROMPT=\$vcs_info_msg_0_
zstyle ':vcs_info:git:*' formats '%F{240}(%b)'
zstyle ':vcs_info:*' enable git

# cpad2
source ~/.cpad2/profile

# mvn
export PATH=/usr/local/bin/apache-maven-3.6.3/bin:$PATH

# Fix no match find when executing rake cmd
setopt nonomatch

# Google Cloud SDK.
export CLOUDSDK_PYTHON=python2.7
if [ -f '~/google-cloud-sdk/path.zsh.inc' ]; then . '~/google-cloud-sdk/path.zsh.inc'; fi
# enables shell command completion for gcloud.
if [ -f '~/google-cloud-sdk/completion.zsh.inc' ]; then . '~/google-cloud-sdk/completion.zsh.inc'; fi

# pyenv
if command -v pyenv 1>/dev/null 2>&1; then
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv init --path)"
fi

# Java 11
export JAVA_HOME=$(/usr/libexec/java_home -v 11)

# tfenv
export PATH="$HOME/.tfenv/bin:$PATH"

# poetry
export PATH="$HOME/.poetry/bin:$PATH"

# Go
export PATH="$HOME/go/bin:$PATH"

# node (nvm)
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm

# load .nvmrc
# place this after nvm initialization!
autoload -U add-zsh-hook
load-nvmrc() {
  local nvmrc_path="$(nvm_find_nvmrc)"

  if [ -n "$nvmrc_path" ]; then
    local nvmrc_node_version=$(nvm version "$(cat "${nvmrc_path}")")

    if [ "$nvmrc_node_version" = "N/A" ]; then
      nvm install
    elif [ "$nvmrc_node_version" != "$(nvm version)" ]; then
      nvm use
    fi
  elif [ -n "$(PWD=$OLDPWD nvm_find_nvmrc)" ] && [ "$(nvm version)" != "$(nvm version default)" ]; then
    echo "Reverting to nvm default version"
    nvm use default
  fi
}
add-zsh-hook chpwd load-nvmrc
load-nvmrc
