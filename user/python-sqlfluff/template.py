pkgname = "python-sqlfluff"
pkgver = "3.4.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-chardet",
    "python-click",
    "python-colorama",
    "python-diff-cover",
    "python-jinja2",
    "python-pathspec",
    "python-platformdirs",
    "python-pytest",
    "python-pyyaml",
    "python-regex",
    "python-tblib",
    "python-tqdm",
]
checkdepends = [
    *depends,
    "python-hypothesis",
]
pkgdesc = "Modular SQL linter and formatter"
license = "MIT"
url = "https://github.com/sqlfluff/sqlfluff"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "09c87fd7021cede30d221d1cafbe055588f392dbc3f7ea1f313b4ca4bb89edc7"


def pre_check(self):
    self.rm("test/core/plugin_test.py")


def post_install(self):
    self.install_license("LICENSE.md")
