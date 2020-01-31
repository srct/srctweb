# SRCTWeb -- the homepage of Mason SRCT

Our own little site on the world wide web.

A static site built with [Jekyll](https://jekyllrb.com/).

# Setup instructions for local development

## 1) Install `git` on your system

`git` is the version control system used for SRCT projects.

### On Linux Based Systems

**with apt:**

Open a terminal and run the following command:

    sudo apt update

This retrieves links to the most up-to-date and secure versions of your packages.

Next, with:

    sudo apt install git

you install `git` onto your system.

### On macOS

We recommend that you use the third party Homebrew package manager for macOS,
which allows you to install packages from your terminal just as easily as you
could on a Linux based system. You could use another package manager (or not
use one at all), but Homebrew is highly reccomended.

To get homebrew, run the following command in a terminal:

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

**Note**: You do NOT need to use `sudo` when running any Homebrew commands, and
it likely won't work if you do.

Next, to make sure Homebrew is up to date, run:

    brew update

Finally we can install git with:

    brew install git

### On Windows

Download Git for Windows here:

[https://git-scm.com/download/win](https://git-scm.com/download/win)

I have also successfully ran the project with Docker on Windows, though you need
access to Hyper-V which is only available on **"Professional"** versions of Windows.

## 2) Clone the srctweb codebase

Now, we're going to clone down a copy of the SRCTWeb codebase from [git.gmu.edu](https://git.gmu.edu/srct/srctweb),
the SRCT code respository with SSH.

**a)** Configure your ssh keys by following the directions at:

**[https://git.gmu.edu/srct/schedules/wikis/Adding-SSH-Keys-to-GitLab](https://git.gmu.edu/srct/schedules/wikis/Adding-SSH-Keys-to-GitLab)**

**b)** Now, on your computer, navigate to the directory in which you want to download the project (ie. perhaps one called `~/development/SRCT`), and run

    git clone git@git.gmu.edu:srct/srctweb.git

## 3) Get SRCTWeb up and running with the method of your choice

Now that we have cloned down the repo you can

    cd srctweb/

and get to working on setting up a development environment!

### Docker

Installing Docker on your system:

* For macOS go here: https://docs.docker.com/docker-for-mac/
* For Windows (**PROFESSIONAL EDITION ONLY**) go here: https://docs.docker.com/docker-for-windows/
* For your specific linux disro go here: https://docs.docker.com/engine/installation/
  * Additionally, you will need to install docker-compose: https://docs.docker.com/compose/install/

Run:

    docker-compose up

If that doesn't work, try:

    sudo docker-compose up

You should see that the server is running by going to [http://localhost:4000](http://localhost:4000) in your browser. Any changes you make to your local file system will be mirrored in the server.

### Installing Jekyll manually

#### Windows

1. Go to https://jekyllrb.com/docs/installation/windows/
2. Press the RubyInstaller link
3. Install the Ruby+Devkit 2.6.4-1 (x64)
4. Go through the installer
5. Open a terminal and type gem install jekyll bundler tzinfo tzinfo-data
6. Go to the folder you installed srctweb and type jekyll serve -s './srctweb' -d './srctweb/_site'
9. Navigate to localhost:4000 in a web browser

#### MacOS

1. Install homebrew if you have not already done it.
2. Type "brew install rbenv ruby-build" to install rbenv, a tool to manage ruby versions.
3. Run the command "rbenv init"
    If you get an error such as:
    # Load rbenv automatically by appending
    # the following to ~/.bash_profile:
    
    try the following: "echo 'eval "$(rbenv init -)"' >> ~/.bash_profile"
4. Install a specific version of rbenv using the command, "rbenv install 2.6.5".
5. Enter the command "rbenv global 2.6.5".
6. Type command "ruby -v" to confirm the ruby version as 2.6.5.
7. "gem install bundler" to install bundler, the tool to download ruby packages.
8. go into the srctweb directory, run cd srctweb again then run "bundle install" to
    install the ruby packages needed for the project.
9. Enter "bundle exec jekyll serve" or "jekyll serve" if the first command fails.
    If you are getting an error saying the port is unavaible, just type "bundle exec jekyll serve --port [portnum].

# Contrubuting

Please read `CONTRIBUTING.md` for specific information and best practices on how
to contribute to the project.
