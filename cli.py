import click


from gig import GIG


@click.command()
@click.option('--lang', type=str, default='None')
def cli(lang):
    ob = GIG()
    if lang == 'None':
        click.echo('Generating empty gitignore'
        'since lang argument not provided')
    else:
        ob.generate(lang)