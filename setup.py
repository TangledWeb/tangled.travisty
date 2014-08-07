from setuptools import setup, PEP420PackageFinder


setup(
    name='tangled.travisty',
    version='0.1.dev0',
    description='Tangled travisty integration (core)',
    long_description=open('README.rst').read(),
    url='http://tangledframework.org/',
    author='Wyatt Baldwin',
    author_email='self@wyattbaldwin.com',
    packages=PEP420PackageFinder.find(include=['tangled']),
    install_requires=[
        'tangled>=0.1a8',
    ],
    extras_require={
        'dev': [
            'tangled[dev]',
        ],
    },
    entry_points="""
    [tangled.scripts]
    travisty = tangled.travisty.command:Command

    """,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
