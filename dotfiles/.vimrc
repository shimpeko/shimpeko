syntax on
" tab
set tabstop=4
set expandtab
set softtabstop=4
set shiftwidth=4
" indent
set smartindent
" show 
set ruler
set title
set showmatch
set matchtime=1
" search
set incsearch
set hlsearch
" enable backspace
set bs=indent,eol,start
" show tabs
set list
set listchars=tab:>-,trail:.

call plug#begin('~/.vim/plugged')
    Plug 'vim-scripts/ruby-matchit'
    Plug 'tpope/vim-endwise'
    Plug 'othree/html5.vim'
    Plug 'google/vim-jsonnet'
    Plug 'derekwyatt/vim-scala'
    Plug 'ain/vim-capistrano'
    Plug 'hashivim/vim-terraform'
    Plug 'rust-lang/rust.vim'
call plug#end()

augroup fileTypeIndent
    autocmd!
    autocmd BufNewFile,BufRead *.iam setlocal tabstop=2 softtabstop=2 shiftwidth=2
    autocmd BufNewFile,BufRead *.jsonnet setlocal sw=2 sts=2 ts=2
    autocmd BufNewFile,BufRead *.yaml setlocal sw=2 sts=2 ts=2
augroup END

let g:jsonnet_fmt_options="-n 2"

autocmd BufNewFile,BufRead *.avcs set syntax=json
