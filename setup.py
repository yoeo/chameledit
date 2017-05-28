#!/usr/bin/env python3

from pathlib import Path

from setuptools import setup, find_packages


def list_resources(basedir, resource_dirs):
    return [
        (str(path.parent), [str(path)])
        for dirname in resource_dirs
        for path in Path(basedir, dirname).glob('**/*') if path.is_file()
    ]


setup(
    name="chameledit",
    author="yoeo",
    version="0.1",
    url="https://github.com/yoeo/chameledit",
    license="MIT",
    description="Web editor that detects programming language, Guesslang Demo",
    install_requires=Path('requirements.txt').read_text().splitlines(),
    packages=find_packages(),
    data_files=list_resources('chameledit', ('static', 'templates')),
    zip_safe=False,
    scripts=['bin/chameledit-gunicorn'],
    entry_points={
        'console_scripts': ['chameledit = chameledit.__main__:main']
    },
)
