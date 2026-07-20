pkgname = "pipx"
pkgver = "1.16.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-docutils",
    "python-hatch_vcs",
    "python-hatchling",
    "python-installer",
]
checkdepends = [
    "python-pytest",
]
depends = [
    "python-argcomplete",
    "python-filelock",
    "python-packaging",
    "python-platformdirs",
    "python-userpath",
]
pkgdesc = "Python tool for installing binaries to venvs"
license = "MIT"
url = "https://github.com/pypa/pipx"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "393f71153ca097c87e1ae044154eac95f8eef21d24a132b64bce4c436ef65b77"
# missing some unknown deps
options = ["!check"]


def init_build(self):
    self.env["SETUPTOOLS_SCM_PRETEND_VERSION"] = f"{pkgver}"


def post_install(self):
    self.install_license("LICENSE")
