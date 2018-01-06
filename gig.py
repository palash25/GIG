import os
import shutil
import pkg_resources


from map import MAP


class GIG(object):
    def __init__(self):
        pass
    
    def generate(self, arg):
        gfile = MAP[arg]
        dest = os.getcwd() + '/.gitignore'
        resource_package = __name__  # Could be any module/package name
        resource_path = '/'.join(('templates', gfile))
        src = pkg_resources.resource_filename(resource_package, resource_path)
        shutil.copy(src, dest)