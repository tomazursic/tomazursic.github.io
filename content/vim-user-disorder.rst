:Title: Vim User Disorder 
:Date: Fri Sep 7 13:48:16 CEST 2018 
:Modified: Jan 17, 2020
:Category: blog 
:Tags: vim, tools 
:Summary: Cheatsheet and notes for (neo)vim editor

.. contents:: Table of Contents

**VUD** 

The vim editor which is always in use, so much that you start smashing into
alien editors with vim commands. If you find somewhere in documents random
characters "jjjkk" or any characters of "jklhzz" there was a vim user in this
file. This acronym is just a dark fun invented by us, back somewhere in time.


Neo(vim)
========

The current plugged list (extensions in use)

.. code-block:: text

  " Comment stuff out
  Plug 'tpope/vim-commentary'

  " Quoting & parenthesizing
  Plug 'tpope/vim-surround'

  " auto-close plugin
  Plug 'rstacruz/vim-closer'

  " Intellisense Engine
  " Plug 'neoclide/coc.nvim', { 'do': 'yarn install' }
  Plug 'neoclide/coc.nvim', {'tag': '*', 'do': { -> coc#util#install()}}

  " Fuzzy search fzf as well using vim-plug
  Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }
  Plug 'junegunn/fzf.vim'

  " Snippet support
  Plug 'honza/vim-snippets'

  " HTML, ccs, js completion tool
  Plug 'mattn/emmet-vim', { 'for': 'html' }

  " Distraction-free writing
  Plug 'junegunn/goyo.vim'

  " Print function signatures in echo area
  Plug 'Shougo/echodoc.vim'

  " Write different documentation styles
  Plug 'kkoomen/vim-doge'

  " === Git Plugins === "
  " Enable git changes to be shown in sign column
  Plug 'mhinz/vim-signify'
  Plug 'tpope/vim-fugitive'

  " === Javascript Plugins === "
  " Typescript syntax highlighting
  Plug 'HerringtonDarkholme/yats.vim'

  " ReactJS JSX syntax highlighting
  Plug 'mxw/vim-jsx'

  " Generate JSDoc commands based on function signature
  Plug 'heavenshell/vim-jsdoc'

  " === Syntax Highlighting === "

  " Syntax highlighting for javascript libraries
  Plug 'othree/javascript-libraries-syntax.vim'

  " Improved syntax highlighting and indentation
  Plug 'othree/yajs.vim'

  " === UI === "
  " File explorer
  Plug 'scrooloose/nerdtree'

  " Material colorscheme
  Plug 'NLKNguyen/papercolor-theme'

  " Customized vim status line
  Plug 'vim-airline/vim-airline'
  Plug 'vim-airline/vim-airline-themes'


Coc Extra:

.. code:: text

  : CocInstall coc-python coc-rls coc-tsserver coc-eslint coc-json coc-prettier coc-emme

Cheatsheet
==========

Operator pending mode
---------------------

.. code:: text

 g~ Swap case
 gu Make lowercase
 gU Make uppercase

Text objects
------------

Bounded
^^^^^^^

.. code:: text

 iw current word
 aw current word + space

 iW current WORD
 aW current WORD + space

 is current sentence
 as current sentence + space

 ip current paragraph
 ap current paragraph + space

Delimited
^^^^^^^^^

.. code:: text

   ab par of ()
   ib inside ()

   aB par of {}
   iB inside {}

   a] par of []
   i] isnide []

   a< par of <>
   i< inside <>

   at par of <xmltags>
   it inside <xmltags>

Operators + text objects
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: text

 d {motion} aw, as, ap

         dap delete a paragraph

 c {motion} iw, it, i"

         ci" change inside "

 g {U, u, ~} aw, ap, it

         gUw make word uppercase
         gUiw make word uppercae

Natural language text editor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: text


      VERBS   MOTIONS OBJECTS
      [cdyv=] [iatf]   [w{"pt)sB]

      ciw hno asr nid gd ee

      vat ira sog uus an ld

      cip hna asr nia gd ee

Normal mode
-----------

This is Vim’s default mode. Typing a letter here doesn’t insert text,
but rather lets you navigate and manipulate text in various ways.

.. code:: text

       gg - beginning of document
       G - end of document
           4G - go to line 4
       b - beginning of previous word
       B - beginnging of previous WORD (like the above except WORD can include punctuation)
       w - next word
       W - next WORD
       e - end of word
       E - end of WORD
       ge - end of previous word
       gE - end of previous WORD
       0 - beginning of line
       $ - end of line

       + - move down by line beginnings
       - - move up by line beginnings

       ^ - first non-blank character
       g_ - last non-blank character
       '. - go to last edited line
       '' - previous cursor position

       gi - go to insert mode on previous cursor position
       gx - go to the URL under the cursor
       ga - show info about character under cursor
       Ctrl-G - show line info

       . - repeat previous command

       f - find character on line
           3fq - third occurrence of 'q'
       F - find character on line, looking backwards
       t - go till the specified character
       T - go till the specified character, looking backwards
       ; - repeat last f, F, t or T command
       , - repeat last f, F, t or T command, backwards

       * - next occurrence of word under cursor
       # - previous occurrence of word under cursor

       4| - jump to column 4

       H - top of screen (high)
       M - middle of screen
       L - bottom of screen (low)

       Ctrl-f - forward one screenful
       Ctrl-b - backward one screenful

       { - previous empty line
       } - next empty line
       % - go to next matching parenthesis
       ) - next sentence
       ( - previous sentence
       ]] - to next section (what a section is depends on the file type)
       ][ - to next closing brace section
       [[ - to previous section
       [] - backwards to closing brace section
       ]m - next method
       [m - previous method
       ]M - end of next method
       [M - end of previous method

       Ctrl-o - retrace movements in file backwards
       Ctrl-i - retract movement in file forwards
       Ctrl-u - up half a page
       Ctrl-d - down half a page

       zz - center screen on cursor
       zt - align top of screen with cursor
       zb - align bottom of screen with cursor

       inplace editing
           r - replace character
           J - join line below to current one

           ~ - toggle case
           g~~ - toggle case of line
           g~$ - toggle case until end of line

           Ctrl-A - increment number beneath cursor
           Ctrl-X - decrement number beneath cursor

           == - autoindent
           =% - autoindent within braces

       entering insert mode
           i - insert mode
           I - insert at beginning of line
           s - substitute character (deletes the character under the cursor and goes into insert mode)
           S - subsitute line (same as doing cc)
           C - substitute from cursor to end of line
           a - append after cursor
           A - append at end of line
           o - open (append) new line below
           O - open (append) new line above

       search
           / - search
               /hello - search for the word 'hello'
               patterns
                   non-greedy match - /http.\{-}

                   including line endings
                       \n - a newline character (line ending)
                       \_s - a whitespace (space or tab) or newline character
                       \_^ - the beginning of a line (zero width)
                       \_$ - the end of a line (zero width)
                       \_. - any character including a newline

           ? - search backwards
           n - repeat search
           N - repeat search in opposite direction
           /\v'.+' - search using 'very magic mode', to avoid having to escape common characters
           /\n\zs[a-z0-9] - use \zs flag to crop selection
           (in this case omitting the \n from the highlighted search result)

       editing window
           q/ - show and edit searches in a buffer
           q: - show and edit history of commands
           q? - show and edit backwards searches

       cc - change entire line
       dd - delete entire line
           4dk - delete 4 lines upwards
       yy - yank line
       yw - yank word
       "zyy - yank line to buffer z
       c - change
       p - paste
       P - paste before cursor
       gp - paste and go to end of text
       gP - paste before cursor and go to end of text
       x - cut
       X - cut before cursor
       D - delete till end of line

       undo and redo
           u - undo
           U - hard undo (back to states before any edits were made)
           Ctrl-r - redo
           g- - go backwards in history tree
           g+ - go forward in history tree
           :earlier 20s

       combining operators, movements and counts
           cw - change word
           ci' - change everything inside quotes
               ci"
               ci<
           cib - change everything inside brackets
           ciB - change everything inside braces
           ct_ - change till underscore
           cT_ - change till underscore (backwards)
           cit - change in tag (XML or HTML)

           dk - delete line above
           3dk - delete the 3 lines above

       windows
           Ctrl-ww - switch window
           Ctrl-wh - move cursor to left-hand window
           Ctrl-wj - move cursor to upper window
               2 Ctrl-wj - move cursor up 2 windows
           Ctrl-wk - move cursor to upwards window
           Ctrl-wl - move cursor to right-hand window
           Ctrl-t - move cursor to top window
           Ctrl-b - move cursor to bottom window
           Ctrl-wq - quit window

           Ctrl-= - even out window sizes
           Ctrl-- - reduce window size
           Ctrl-+ - increase window size
           z6<CR> - make window 6 lines high

           Ctrl-> - increase window width
           Ctrl-< - decrease window width

           Ctrl-x - exchange the window with the next one

           Ctrl-H - move window to be left column
           Ctrl-J - move window to be bottom row
           Ctrl-K - move window to be top row
           Ctrl-L - move window to be right column

       open current buiffer in new tab
           Ctrl + w + Shift t

       switching tabs
           Cmd-shift [ - previous tab
           Cmd-shift ] - next tab

       q - record macro
           qa - record marcro in register 'a'
           do something special
           press q again to stop recording
           16@a - run the macro 16 times
           "ap - paste the contents of the 'a' macro
           :%normal @b - repeat until end of file
           @@ - repeat last macro

       registers (any time you delete or yank text it goes into a register)
           :reg - show contents of registers
           "1p - paste from register 1.
           "+p - paste from system clipboard

       marks
           :marks - show marks

           lowercase marks (mark positions and jump around in the current file)
               create
                   ma
                   mb
               jump to
                   'a
                   'b

           uppercase marks (mark positions and jump around between different files)
               create
                   mA
                   mB
               jump to
                   'A
                   'B

           :delm - delete a mark

           jumping to marks
               use ` to move position-wise and ' to move line-wise

               `[ - jump to beginning of last yanked or changed text
               `] - jump to end of last yanked or changed text
               `< - jump to beginning of last visual selection
               `> - jump to end of last visual selection

       tags
           vim will read a 'tags' file automatically

           Ctrl-] - jump to definition
           Ctrl-t - jump back from definition

           g] - list matching tags

           :tag _initInputField - jump the function definition of _initInputField
           :tag /placeholder - jump to tag matching the text 'placeholder'

           :ptag placeholderUrl - open tag in preview window
           :tselect afterSave - select from multiple matching tags
           :tjump url - jump to unique tag, or list non-unique ones

       spell checking
           :set spell
           ]s - next spelling mistake
           [s - previous spelling mistake
           z= - bring up list of suggestions for word under cursor
           1z= - replace word with first suggested spelling
           zg - mark word as good in spell list
           zw - mark word as bad in spell list

           zug - undo adding as good
           zuw - undo addings as bad

           ~/.vim/spell/en.utf-8.add

Insert mode
-----------

This is where you actually insert text. You can type i to get into
insert mode. Keep in mind that while the commands below are handy, Vim
works best when you stay out of insert mode as much as possible. In
other words, go into insert mode only to enter text, and get back into
normal mode as soon as possible.

.. code:: text

       3iGo - insert "Go" 3 times
       Ctrl-P - autocomplete
       Ctrl-X  Ctrl-O - omnicomplete

       Ctrl-y - duplicate line above, character-by-character
       Ctrl-e - duplicate line below, character-by-character

       Ctrl-t - indent line
       Ctrl-d - unindent line

       Ctrl-r {reg} - insert from register
           Ctrl-r =2+2 - insert '4' from expression register
           Ctrl-r =sqrt(4)

           :help function-list

       inserting special characters, digraphs
           Ctrl-K
               Type approximation of the character, e.g.
                   a: for ä
                   14 for ¼
               :dig to reference these
           Ctrl-V

       editing while in insert mode
           Ctrl-w - delete word before cursor
           Ctrl-u - delete line before cursor
           Ctrl-rx - insert contents of register x
           Ctrl-t - increase line indent
           Ctrl-d - decrease line indent

       paste laste yanked content in insert mode
           Ctrl + r *

       leaving
           <Esc>
           Ctrl-[

Visual mode
-----------

This mode lets you make visual selections of text.

.. code:: text


       v - start selecting
       V - visual line mode (follow with j or k to select up or down)
       vib - select visually within brackets
       viB - select visually within braces
       viW - select visually within word (or URL or filename)
       v2ap - select 2 paragraphs visually
       gv - previous visual selection

       gv - reselect what was previously selected
       = - fix indentation on visually selected text

       search within visual selection
           make the selection
           hit escape
           /\%Vwhat_to_search

       visual block mode
           Ctrl-V
           move around to make a selection, e.g - j
           I to insert and type something
           esc to exit the mode and insert the characters

           c - change
           d - delete
           o - toggle to opposite

Command line mode
-----------------

Typing a colon gives you access to many commands.

.. code:: text

       Ctrl-b - beginning of command line
       Ctrl-e - end of command line
       Ctrl-w - delete word
       Ctrl-r - insert a register
       Ctrl-r Ctrl-w - insert word from under cursor
       Ctrl-f - edit using normal mode
       @: - repeat previous ex command

       :cd ~/Projects/myproject
           cd %:h - change to the directory of the current file
       :pwd
       :so ~/.vimrc
       :!ls
       :sp a.txt - split window and edit a.txt
       :vsp b.txt

       :enew - edit a new buffer in the current window

       :r - read in a file
           :185r read in line 185

       :w - write a file
           :w test.txt

       :normal - do something as if in normal mode

       :put - put results on a new line
           :put =4*2
           :put =system('echo $RANDOM')

       set wrap! - toggle line wrapping
       set nowrap
       set wrap

       external command
           :%! markdown - filter buffer via the external 'markdown' command
           :%! tidy - filter buffer via html tidy
           :!wc % - word count

       ranges
           :15,30d - delete lines 15 - 30
           :15,30m $ - move lines 15 - 30 to the end
           :15,30>> - indent lines 15 - 30

       command history
           : and the up key

       filename
           use a % sign on the command line to denote the current file
           :! echo %
           :so %

           :! markdown % > %:p:r.html
           :help filename-modifiers

       search and replace
           :%s/old/new - search and replace (first occurrence in each line)
           :%s/old/new/g - search and replace globally
           :%s/old/new/gc - search and replace with confirmations
           :%s/\%Vold/new/g - search and replace visual selection
           d/pattern - delete 'pattern'
           :5,12s/old/new/g - search and replace within range
           :%s/\s\+$//e - strip whitespace from ends of lines

           :%s/<br>\n<br>/\r<\/p>\r<p>/g - replace br with p

           :g/test/d - delete all lines that match 'test'
           :g!/test/d - delete all lines that don't match 'test'
           :g/\t/d - delete all lines with a tab
           :g/^$/d - delete blank lines
           :g!/_/d - delete lines without underscores

           replace line breaks
               :%s/<Ctrl-V><Ctrl-M>//g
               Where <Ctrl-V><Ctrl-M> means type Ctrl+V then Ctrl+M.

       move
           :m 12 - move current line to after line 12
           :m 0 - move current line to before first line
           :m $ - move current line to after last line
           :m7 - move current line to line 7
           :4m7 - move line 4 to line 7
           :4m$ - move line 4 the end of document

       copy
           :3co7 - copy line 3 after line 7
           :3t7 - same as above
           :3t. - copy line 3 to after current line

           :sort - sort lines alphabetically
           :retab
           :retab! - spaces to tabs
           :changes
           :dig - digraphs
           :color - show current colorscheme

       :%TOhtml - generate HTML page that looks like the current view
       :w !sudo tee % - write current file with sudo, to avoid file permission error

       buffers
           :buffers
           :ls
           :files

           :b3 - display buffer 3
           :bn - next buffer
           :bp previous buffer
           Ctrl-6 - switch between recent buffers

           :bd
           :bdel
           :5,999bd

           :%bd - delete all buffers

           :bdel galleries <Ctrl-a> - complete all matches

           status column
               h is hidden
               + means unsaved changes

       args
           :args
           :args ~/Dropbox/documents/unix.txt ~/Dropbox/documents/mac.txt
           :args *.txt
           :args `cat table_of_content.txt`
           :args `find  - -type f`

           argdo
               :args *.txt
               :argdo %s/\a/*/g
               :argdo update

               " OR"

               :argdo %s/foo/buz/g | update

               search and replace
                   :args `git grep -l findme`
                   :argdo %s/findme/replacement/gc
                   :argdo update

       grep (search across multiple files)
           :vimgrep /pr( **/*.ctp

       quickfix window
           :cw
           :cnext
           :cprev

       fileformat
           :set ff? - show fileformat

           convert in current buffer
               :setlocal ff=unix
               :w

       insert special characters
           Ctrl-v
               :%s/Ctrl-v Ctrl-m//g becomes :%s/^M//g


       Global replace
       First try the substitute and than make global run
       Using: ag

           : args `ag -l some_word`
           : argdo %s/some_word*./foo/g | w

       Global search and replace
       Using: fzf

           1) Search for files contains pattern
               <leader>F

           2) Inset pattern
              :File <search_pattern>

           3) Select all matches
               Alt + a

           4) Substitute
              :cfdo %s/foo/baz/g

TIPS
----

Scrolling
^^^^^^^^^

For scrolling avoid ``j`` and ``k``.

-  If you need to scroll, it’s better to use ;

.. code:: text

   Ctrl-e and Ctrl-y

-  If you need to scroll faster, use:

.. code:: text

   Ctrl-d and Ctrl-u.

-  If you really want to blaze through a file, use:

.. code:: text

   Ctrl-f or Ctrl-b.


Install Neovim
==============

Install on ubuntu::

    $ sudo apt-get install software-properties-common
    $ sudo apt-get install python-dev python-pip python3-dev python3-pip
    $ sudo apt-add-repository ppa:neovim-ppa/stable
    $ sudo apt-get update
    $ sudo apt-get install neovim

`Link install: <https://github.com/neovim/neovim/wiki/Installing-Neovim>`_

Transition
-----------

Set `neovim` to use `vimrc`

Create `nvim` config::

    mkdir ~/.config/nvim && cd !$ && touch init.vim

Add to `init.vim`::

    set runtimepath^=~/.vim runtimepath+=~/.vim/after
    let &packpath = &runtimepath
    source ~/.vimrc


View help for transition::

    :help nvim-from-vim 

`Link nvim-from-vim: <https://neovim.io/doc/user/nvim.html#nvim-from-vim>`_

History
=======

The Evolution:

.. code:: text

       ed >> em >> ex >> vi >> vim

**The Ex Editor**

Ex is a ‘line editor’ Vim is a ‘screen editor’ Ex is sub-editor within
Vim. Amen.
