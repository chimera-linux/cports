pkgname = "python-execnet"
pkgver = "2.0.2"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-hatch_vcs",
    "python-hatchling",
]
checkdepends = [
    "python-pytest",
]
pkgdesc = "Distributed python deployment and communication"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/pytest-dev/execnet"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7500bdc398c39558c04e12eb52075af7365a40f90dec08593f182e8ed733f91e"


def init_build(self):
    self.env["SETUPTOOLS_SCM_PRETEND_VERSION"] = f"{pkgver}"


def post_install(self):
    self.install_license("LICENSE")
