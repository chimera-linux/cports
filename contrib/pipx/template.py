pkgname = "pipx"
pkgver = "1.4.1"
pkgrel = 0
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
sha256 = "91766031371a7f46148f7919957a7e4d43c4d440aeac4910989ba9a34b3007e3"
# missing some unknown deps
options = ["!check"]


def init_build(self):
    self.env["SETUPTOOLS_SCM_PRETEND_VERSION"] = f"{pkgver}"


def post_install(self):
    self.install_license("LICENSE")
