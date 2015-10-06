SRCTweb
===

Our own little site on the world wide web

On Contributing
---

SRCTweb welcomes all the help it can get. Even if you don't feel like you can be helpful the more technical aspects, we definitely need designers, technical writers, and testers.

There are many things that can be done with this project (see the "To Do" section), but sometimes it's the small things that count, so don't be afraid of contributing just a small spelling mistake.

If you need help at all please contact and SRCT member. We want people to contribute, so if you are struggling, or just want to learn we are more than willing to help.

The project lead for this project is **Daniel Bond**. *dbond2@gmu.edu*

Please visit the [SRCT Wiki](http://wiki.srct.gmu.edu/) for more information on this and other SRCT projects, along with other helpful links and tutorials.

Setup
---

To get started, you'll need the following installed:
* [Git](http://git-scm.com/book/en/Getting-Started-Installing-Git)
* [Python 2.7.3](http://www.python.org/download/)
* [Pip](http://www.pip-installer.org/en/latest/install.html)
* [virtualenv](http://www.virtualenv.org/en/latest/index.html#installation)

Open a terminal window and type in the following commands. (If you're on Windows, use [Cygwin](http://www.cygwin.com/). This will create a local, workable copy of the project.)

(set up pip and virtualenv)

```bash
bash
git clone git@git.gmu.edu:srct/srctweb.git
cd srctweb/
pip install -r requirements.txt
cd srctweb/
python srctweb.py
```

To-do
---

Note-- this should also be on the wiki

**1.1 Release**
* set up database for people, meeting date on index page, projects
* figure out where to put a link to meeting notes
* Jeykll for meeting notes, finish hackmason (both not in this repository)
* Figure out parallaxjs for front page
* Figure out intellectual property with GMU
* finish writing privacy policy
* affix js for documents navigation-- example http://www.bootstrapzero.com/bootstrap-template/affix-sidebar

---

TODO Re: OpenHatch:

* Make mobile friendly at least kinda
* Improve top left title. Is hacked together with a visibility: hidden div and uses way more space than it needs

**S**tudent - **R**un **C**omputing and **T**echnology (*SRCT*, pronounced "circuit") is a student organization at George Mason University which enhances student computing at Mason. SRCT establishes and maintains systems which provide specific services for Mason's community.
