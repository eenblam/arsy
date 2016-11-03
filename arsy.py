#!/usr/bin/env python

import click
import sys
import os
import subprocess

@click.group()
@click.pass_context
def click(ctx):
    #TODO Get ons and offs & arsy path
    ctx.obj['.bashrc'] = ''
    ctx.obj['.arsy'] = ''
    ctx.obj['on'] = []
    ctx.obj['off'] = []

def move(old, new, *args):
    #TODO: Should I sys.exit(1) if an error occurred?
    # If so, should I try processing other args before raising error?
    for arg in args:
        full_path = os.path.join(ctx.obj['.arsy'], full_path)
        in_old = arg in old
        in_new = arg in new
        does_not_exist = not (in_old or in_new)
        good_to_move = in_old and not in_new
        already_new = in_new and not in_old
        in_both = in_old and in_new
        
        if good_to_move:
            # Great!
            # mv arg.off arg.on
            # os.rename, since shutil.move doesn't keep metadata

        elif does_not_exist:
            # Alert the user. Couldn't find arg + '.off' or arg + '.on'.

        elif already_new:
            # No big deal; just let the user know

        elif in_both:
            # Bad! Alert the user.

@click.command()
@click.pass_context
def on(ctx, *args):
    ons = ctx.obj['on']
    offs = ctx.obj['off']
    move(offs, ons, *args)

@click.command()
@click.pass_context
def off(ctx, *args):
    ons = ctx.obj['on']
    offs = ctx.obj['off']
    move(ons, offs, *args)


@click.command()
@click.pass_context
def list(ctx, *args):
    pass

@click.command()
@click.pass_context
def path(ctx):
    click.echo(ctx.obj['.arsy'])

@click.command()
@click.pass_context
def source(ctx):
    # . .bashrc
    # Guess I need home directory?

if __name__ == '__main__:
    cli(obj={})
