:title: Git Notes
:date: 2017-07-08
:tags: git, linux
:category: blog
:slug: git
:summary: Notes using git

Git Tips
========


Reset
-----

Reset current git repo to match remote

.. code-block:: lua

    # Save work
    git co -b save-work
    git co master

    git fetch origin
    git reset --hard origin/master

Remove wrong commit from master.
Reset reassign the branch pointer

.. code-block:: lua

    HEAD   is the commit currently siting on
    ^HEAD  this commit parent
    ^^HEAD this commit grandparent

    $ git co master
    $ git reset --hard ^HEAD

Reset last commit

.. code-block:: lua

    git reset --hard HEAD~1


Contribute
----------

1. Make Fork on webpage
2. Create local clone
3. Add remote upstrem to original repo

.. code-block:: shell

    $ git remote add upstream https://github.com/octocat/Spoon-Knife.git

4. View remote

.. code-block:: shell

    $ git remote -v

5. Sync a fork

.. code-block:: shell

    $ git fetch upstream

6. Branch set to track upsream master

.. code-block:: shell

    $ git branch --set-upstream-to=upstream/master master

7. Create new brnch for working on

.. code-block:: shell

    $ git checkout -b <branch-name>

8. Create changes, commit and push to origin remote

.. code-block:: shell

    $ git push -u origin <branch-name>

9. Create Pull Request in GUI
