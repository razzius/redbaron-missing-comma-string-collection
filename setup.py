import setuptools

requires = [
    "flake8 > 3.0.0",
]

setuptools.setup(
    name="flake8_missing_commas_string_collection",
    license="MIT",
    version="0.1.0",
    description="Warns about missing commas in a string collection.",
    author="Razzi Abuissa",
    author_email="razzi@abuissa.net",
    url="https://github.com/razzius/flake8-unused-arguments",
    packages=[
        "flake8_missing_commas",
    ],
    install_requires=requires,
    entry_points={
        'flake8.extension': [
            'R101 = flake8_missing_commas:MissingCommasPlugin',
        ],
    },
    classifiers=[
        "Framework :: Flake8",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
