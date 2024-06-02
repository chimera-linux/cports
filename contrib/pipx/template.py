pkgname = "pipx"
pkgver = "1.6.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatch_vcs",
    "python-hatchling",
    "python-installer",
]
checkdepends = [
    "python-pytest",
]
depends = [
    "python-argcomplete",
    "python-packaging",
    "python-platformdirs",
    "python-userpath",
]
pkgdesc = "Python tool for installing binaries to venvs"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/pypa/pipx"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "427bd838bff3c4e5efcc39858eb5e1b86cc5e3468ad939ae44312ac5bb3405ad"
# missing some unknown deps
options = ["!check"]


def init_build(self):
    self.env["SETUPTOOLS_SCM_PRETEND_VERSION"] = f"{pkgver}"


def post_install(self):
    self.install_license("LICENSE")
