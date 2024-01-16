pkgname = "python-ptyprocess"
pkgver = "0.7.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
    "python-wheel",
]
checkdepends = ["bash", "python-pytest"]
depends = ["python"]
pkgdesc = "Run subprocesses in pseudo-terminals"
maintainer = "psykose <alice@ayaya.dev>"
license = "ISC"
url = "https://github.com/pexpect/ptyprocess"
source = f"$(PYPI_SITE)/p/ptyprocess/ptyprocess-{pkgver}.tar.gz"
sha256 = "5c5d0a3b48ceee0b48485e0c26037c0acd7d29765ca3fbb5cb3831d347423220"


def post_install(self):
    self.install_license("LICENSE")
