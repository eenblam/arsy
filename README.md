# Arsy
Arsy is a tool for managing the contents of your `.bashrc`.

Basically, you divide the contents of your `.bashrc` file into a bunch of smaller scripts in `~/.arsy`.
Arsy is just a CLI interface for toggling whether or not a particular script is sourced
whenever you start a login shell session.
You could accomplish the same effect with `mv ~/.arsy/a.on ~/.arsy/a.off`;
Arsy just shaves off a bit of typing and thinking.

This is a tool for people who frequently find themselves working from a new system, but want to be able to manage their disparate configurations in a convenient way. For instance, paths will differ significantly between OSX and Debian. Source control your `.arsy` folder with the rest of your dotfiles. Whenever you clone your dotfiles repo to a new machine, just use `arsy on ...` to enable the parts of your .bashrc that are relevant to your current environment. E.g. if you have `~/.arsy/macpaths.off` and `~/.arsy/debpaths.on` when you clone your dotfiles, you can just run `arsy on macpaths; arsy off debpaths`.

## Installation
You'll need Python, along with `pip` and `setuptools`.
To install:

```bash
git clone https://github.com/eenblam/arsy
cd arsy
python setup.py install
```

## Usage

Usage of existing features:

```bash
$ arsy list # Basically `ls -l ~/.arsy`
# a.on
# b.off
$ arsy list on
$ arsy on a && arsy list
# a.on
# b.off
$ arsy off a b && arsy list
# a.off
# b.off
```

Here's what your `.bashrc` should look like:

```bash
#!/bin/bash
# .bashrc

for f in ~/.arsy/*.on
do
    if [ -f  $f ]; then
        . $f
    fi
done
```

Usage of planned features:

```bash
$ arsy list
# a.on
# b.off
$ arsy freeze works-on-my-machine
$ arsy off a && arsy list
# a.off
# b.off
$ arsy thaw works-on-my-machine && arsy list
# a.on
# b.off
```
