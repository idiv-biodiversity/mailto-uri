import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name = "mailto-uri",
    version = "1.1.0",
    author = "Christian Krause",
    author_email = "christian.krause@idiv.de",
    description = "create mailto URIs",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/idiv-biodiversity/mailto-uri",
    install_requires = [
        'argparse',
        'python-frontmatter'
    ],
    classifiers = (
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ),
    packages = setuptools.find_packages(),
    entry_points = {
        'console_scripts': [
            'mailto-uri = mailto_uri.cli:main',
        ],
    }
)
