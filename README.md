# Arsy
Arsy is a tool for managing the contents of your `.bashrc`.

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

Milestone 1 Usage:

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
$ arsy source # Same as `. ~/.bashrc`; possibly easier to type
```

Milestone 2 Usage:

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
