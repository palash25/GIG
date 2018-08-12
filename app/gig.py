import os
import shutil
import pkg_resources
import click

from .map import MAP


class GIG(object):
    __base = os.getcwd()
    __dest = __base + '/.gitignore'
    __git = __base + '/.git'

    def __init__(self):
        pass

    def gi_not_exists(self, gi_dest):
        if os.path.isfile(gi_dest):
            return False
        else:
            return True

    def git_init(self):
        if os.path.isdir(self.__git):
            return True
        else:
            return False

    def process(self, arg):
        gfile = MAP[arg]
        resource_package = __name__
        resource_path = '/'.join(('templates', gfile))
        src = pkg_resources.resource_filename(resource_package, resource_path)
        shutil.copy(src, self.__dest)
        click.echo(click.style("[SUCC] GITIGNORE generated.", fg='green'))

    def generate(self, arg):
        if not self.git_init():
            click.echo(
                click.style(
                    "[WARN] Git is not initialized yet", fg='yellow'))
            if click.confirm(
                    'Do you want to initialize GIT in this directory?',
                    abort=False):
                os.system('git init .')
            else:
                click.echo(
                    click.style(
                        "[INFO] GITIGNORE was not generated.", fg='blue'))
                quit()

        if self.gi_not_exists(self.__dest):
            self.process(arg)
        else:
            click.echo(
                click.style(
                    "[WARN] GITINGNORE already exists.", fg='yellow'))
            if click.confirm('Do you want to overwrite?', abort=False):
                self.process(arg)
