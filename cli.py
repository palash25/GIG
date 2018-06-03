import click
import os


from app.gig import GIG


@click.command()
@click.option('--lang', type=str, default='None')
def cli(lang):
    ob = GIG()
    if lang == 'None':
        click.echo(click.style("[INFO] Empty GITIGNORE generated,"
                               "if one doesn\'t already exists.", fg='blue'))
        os.system('touch .gitignore')
    else:
        ob.generate(lang)

