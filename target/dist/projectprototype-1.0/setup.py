#!/usr/bin/env python
#   -*- coding: utf-8 -*-

from setuptools import setup
from setuptools.command.install import install as _install

class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()

if __name__ == '__main__':
    setup(
        name = 'projectPrototype',
        version = '1.0',
        description = 'Sistema para gestionar proceedings de eventos academicos.',
        long_description = 'Este proyecto facilita la publicacion, revision y gestion de trabajos para los eventos academicos.',
        long_description_content_type = None,
        classifiers = [
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python'
        ],
        keywords = '',

        author = '',
        author_email = '',
        maintainer = '',
        maintainer_email = '',

        license = '',

        url = 'https://github.com/LeoGB29/projectPrototype',
        project_urls = {},

        scripts = [],
        packages = [],
        namespace_packages = [],
        py_modules = ['app'],
        entry_points = {},
        data_files = [],
        package_data = {},
        install_requires = [
            'Flask',
            'Flask-SQLAlchemy'
        ],
        dependency_links = [],
        zip_safe = True,
        cmdclass = {'install': install},
        python_requires = '',
        obsoletes = [],
    )
