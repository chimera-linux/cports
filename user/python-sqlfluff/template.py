pkgname = "python-sqlfluff"
pkgver = "3.3.1"
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
sha256 = "20251edf134121af9c29957c5d648c1c8be376e259a6ce45e032a9c614f130cc"


def pre_check(self):
    self.rm("test/core/plugin_test.py")


def post_install(self):
    self.install_license("LICENSE.md")
