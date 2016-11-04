#!/usr/bin/env python

import click
from os import listdir, rename
from os.path import expanduser, isfile, join
import subprocess

@click.group()
@click.pass_context
def cli(ctx):
    #TODO Allow argument for alternate .arsy location

    home = expanduser('~')
    ctx.obj['.bashrc'] = join(home, '.bashrc')
    arsy = join(home, '.arsy')
    ctx.obj['.arsy'] = arsy

    files = sorted(f for f in listdir(arsy) if isfile(join(arsy, f)))
    ctx.obj['files'] = files

    ctx.obj['.on'] = [fname[:-3] for fname in files if fname.endswith('.on')]
    ctx.obj['.off'] = [fname[:-4] for fname in files if fname.endswith('.off')]

def mv(source, destination, root=None):
    """Moves file from source to destination via os.rename.

    Does not work across disks.
    Assumes absolute paths unless root is given.
    """
    if root is not None:
        src = join(root, source)
        dst = join(root, destination)
    else:
        src = source
        dst = destination

    try:
        rename(src, dst)
        click.echo('Moved {} to {}'.format(src,dst))
    except OSError:
        # src does not exist or dst is protected
        #TODO Need to figure out how to handle...
        # ...shouldn't happen due to logic in move, but filesystem mutates.
        pass

def move(ctx, old_ext, new_ext, *args):
    for arg in args:
        in_old = arg in ctx.obj[old_ext]
        in_new = arg in ctx.obj[new_ext]

        does_not_exist = not (in_old or in_new)
        good_to_move = in_old and not in_new
        already_new = in_new and not in_old
        in_both = in_old and in_new

        arsy = ctx.obj['.arsy']
        old = arg + old_ext
        new = arg + new_ext

        if good_to_move:
            # Great!
            # os.rename, since shutil.move doesn't keep metadata
            mv(old, new, root=arsy)

        elif does_not_exist:
            # Alert the user. Couldn't find arg + '.off' or arg + '.on'.
            first, second = sorted((old,new))
            click.echo("Couldn't find {} or {} in {}."
                    .format(first, second, arsy))
            continue

        elif already_new:
            # No big deal; just let the user know
            click.echo("{} is already {}.".format(arg, new_ext[1:]))
            continue

        elif in_both:
            # Bad! Alert the user.
            click.echo("Both {} and {} exist. No action taken!"
                    .format(*sorted((old, new))))
            continue

@cli.command()
@click.argument('script', nargs=-1)
@click.pass_context
def on(ctx, script):
    move(ctx, '.off', '.on', *script)

@cli.command()
@click.argument('script', nargs=-1)
@click.pass_context
def off(ctx, script):
    move(ctx, '.on', '.off', *script)

@cli.command()
@click.pass_context
def list(ctx):
    on = [f + '.on' for f in ctx.obj['.on']]
    off = [f + '.off' for f in ctx.obj['.off']]
    for fname in sorted(on):
        click.echo(fname)
    for fname in sorted(off):
        click.echo(fname)

@cli.command()
@click.pass_context
def path(ctx):
    click.echo(ctx.obj['.arsy'])

@cli.command()
@click.pass_context
def source(ctx):
    # . .bashrc
    click.echo('Sorry, you need to run `. ~/.bashrc` yourself.')

def main():
    cli(obj={})

if __name__ == '__main__':
    main()
