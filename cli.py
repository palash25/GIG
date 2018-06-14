import click
import os

from app.map import MAP
from app.gig import GIG


@click.command()
@click.option('--lang', type=str, default='None')
def cli(lang):
    ob = GIG()
    if lang == 'None':
        click.echo(click.style("[INFO] Empty GITIGNORE generated,"
                               "since lang argument is empty.", fg='blue'))
        os.system('touch .gitignore')
    else:
        ob.generate(lang)


@click.command()
@click.option('--listall', help='Lists all the supported Languages')
def list_all():
    print('hello')
