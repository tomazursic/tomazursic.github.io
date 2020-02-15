title: Setup Pelican
date: Wed May 3 7:10:56 CEST 2017
category: blog
tags: python, pelican
summary: Let play with static site generator to reorder mess of memories

### Install Pelican

```sh
$ pip install pelican ghp-import Markdown
```

### Create github page

Create empty new repository on GitHub, with name <username>.github.io

Example:

```text
https://github.com/username/username.github.io
```

### Setup git repository

```sh
$ git clone https://github.com/username/username.github.io blog
$ cd blog

$ git checkout -b content
Switched to a new branch 'content'
```

### Configure Pelican

```sh
$ pelican-quickstart
```

Output:

```text
Welcome to pelican-quickstart v4.1.1.

This script will help you create a new Pelican-based website.

Please answer the following questions so this script can generate the files
needed by Pelican.

> Where do you want to create your new web site? [.]
> What will be the title of this web site? Blog
> Who will be the author of this web site? <your-username>
> What will be the default language of this web site? [en]
> Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) n
> Do you want to enable article pagination? (Y/n)
> How many articles per page do you want? [10]
> What is your time zone? [Europe/Paris] Europe/Ljubljana
> Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) y
> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) y
> Do you want to upload your website using FTP? (y/N) n
> Do you want to upload your website using SSH? (y/N) n
> Do you want to upload your website using Dropbox? (y/N) n
> Do you want to upload your website using S3? (y/N) n
> Do you want to upload your website using Rackspace Cloud Files? (y/N) n
> Do you want to upload your website using GitHub Pages? (y/N) y
> Is this your personal page (username.github.io)? (y/N) y
Done. Your new project is available at /Users/username/blog
```

### Liftoff

Add all the Pelican-generated files to the content branch of the local Git repo, commit the changes, and push the local changes to the remote repo hosted on GitHub by entering:

    $ git add .
    $ git commit -m 'initial pelican commit to content'
    $ git push origin content

### Write content

### Publish

Run Pelican to generate the static HTML files in output:

    $ pelican content -o output -s publishconf.py

Use ghp-import to add the contents of the output directory to the master branch:

```sh
    $ ghp-import -m "Generate Pelican site" --no-jekyll -b master output
```

Push the local master branch to the remote repo:

    $ git push origin master

Commit and push the new content to the content branch:

    $ git add content
    $ git commit -m 'added a first post, a photo and an about page'
    $ git push origin content


### Syntax Highlights with Pygments

View avaiable options

```python

>>> from pygments.styles import STYLE_MAP
>>> STYLE_MAP.keys()
['monokai', 'manni', 'rrt', 'perldoc',
'borland', 'colorful', 'default',
'murphy', 'vs', 'trac', 'tango',
'fruity', 'autumn',
'bw', 'emacs', 'vim', 'pastie', 'friendly', 'native']
```

Generate style file and add to `base.html`

```sh
 $ cd thems/<theme-name>/css
 $ pygmentize -S monokai -f html -a .highlight > pygments_vim.css
```
