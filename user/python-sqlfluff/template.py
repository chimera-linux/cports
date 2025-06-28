pkgname = "python-sqlfluff"
pkgver = "3.4.1"
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
sha256 = "f66fad38f31ae453705ffa9d7ea164e9dbf2b94970216a97b3d39e961728e173"


def pre_check(self):
    self.rm("test/core/plugin_test.py")


def post_install(self):
    self.install_license("LICENSE.md")
