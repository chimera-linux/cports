pkgname = "pipx"
pkgver = "1.2.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
]
checkdepends = [
    "python-pytest",
]
depends = [
    "python-argcomplete",
    "python-colorama",
    "python-packaging",
    "python-platformdirs",
    "python-userpath",
]
pkgdesc = "Python tool for installing binaries to venvs"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/pypa/pipx"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "4ccfb259ce7036c808397ee131de53ea4283fcbfe06c9fb23dcc84c440e3d09d"
# missing some unknown deps
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
