pkgname = "python-mediafile"
pkgver = "0.12.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-flit_core", "python-installer"]
depends = ["mutagen", "python-six"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Handles low-level interfacing for file tags in Python"
maintainer = "Justin Berthault <justin.berthault@zaclys.net>"
license = "MIT"
url = "https://github.com/beetbox/mediafile"
source = f"$(PYPI_SITE)/m/mediafile/mediafile-{pkgver}.tar.gz"
sha256 = "d75d805a06ed56150dbcea76505e700f9809abd9e98f98117ae46f5df2ccf1d7"


def post_install(self):
    self.install_license("LICENSE")
