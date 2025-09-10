pkgname = "python-tornado"
pkgver = "6.5.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "python-alabaster",
    "python-babel",
    "python-black",
    "python-cachetools",
    "python-certifi",
    "python-chardet",
    "python-charset-normalizer",
    "python-click",
    "python-colorama",
    "python-distlib",
    "python-docutils",
    "python-filelock",
    "python-flake8",
    "python-idna",
    "python-imagesize",
    "python-jinja2",
    "python-markupsafe",
    "python-mccabe",
    "python-mypy",
    "python-packaging",
    "python-pathspec",
    "python-platformdirs",
    "python-pluggy",
    "python-pycodestyle",
    "python-pyflakes",
    "python-pygments",
    "python-requests",
    "python-snowballstemmer",
    "python-sphinx",
    "python-sphinxcontrib-applehelp",
    "python-sphinxcontrib-devhelp",
    "python-sphinxcontrib-htmlhelp",
    "python-sphinxcontrib-jquery",
    "python-sphinxcontrib-jsmath",
    "python-sphinxcontrib-qthelp",
    "python-sphinxcontrib-serializinghtml",
    "python-urllib3",
    "python-wheel",
]
checkdepends = ["python-pytest"]
pkgdesc = "Python3 web framework and asynchronous networking library"
license = "Apache-2.0"
url = "https://www.tornadoweb.org"
source = f"$(PYPI_SITE)/t/tornado/tornado-{pkgver}.tar.gz"
sha256 = "ab53c8f9a0fa351e2c0741284e06c7a45da86afb544133201c5cc8578eb076a0"


def post_install(self):
    self.install_license("LICENSE")


def init_check(self):
    self.make_check_args = [
        "--ignore=tornado/test/iostream_test.py",
    ]
