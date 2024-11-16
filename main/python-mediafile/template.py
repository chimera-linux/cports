pkgname = "python-mediafile"
pkgver = "0.13.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-flit_core", "python-installer"]
depends = ["mutagen", "python-filetype"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Handles low-level interfacing for file tags in Python"
maintainer = "Justin Berthault <justin.berthault@zaclys.net>"
license = "MIT"
url = "https://github.com/beetbox/mediafile"
source = f"$(PYPI_SITE)/m/mediafile/mediafile-{pkgver}.tar.gz"
sha256 = "de71063e1bffe9733d6ccad526ea7dac8a9ce760105827f81ab0cb034c729a6d"


def post_install(self):
    self.install_license("LICENSE")
