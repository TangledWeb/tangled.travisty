from setuptools import setup, find_packages


setup(
    name='tangled.travisty',
    version='0.1.dev0',
    description='Tangled travisty integration (core)',
    packages=find_packages(),
    install_requires=(
        'tangled>=0.1.dev0',
    ),
    extras_require={
        'dev': (
            'tangled[dev]',
            'nose>=1.3.0',
        ),
    },
    entry_points="""
    [tangled.scripts]
    travisty = tangled.travisty.command:Command

    """,
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ),
)
