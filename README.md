# Arsy
Arsy is a tool for managing the contents of your `.bashrc`.

Basically, you replace your `.bashrc` file with a bunch of smaller scripts in `~/.arsy`.
Arsy is just a CLI interface for toggling whether or not a particular script is sourced
whenever you start a login shell session.
You could accomplish the same effect with `mv ~/.arsy/a.on ~/.arsy/a.off`;
Arsy just shaves off a bit of typing and thinking.

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

## Contributing
This is a pretty small project, but contributions are welcome.
Tests are written in PyTest.
PR's should come with reasonable, passing tests,
and they shouldn't break any that previously passed.

You can run the test suite with `python setup.py test`.
