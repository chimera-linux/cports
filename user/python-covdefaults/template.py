pkgname = "python-covdefaults"
pkgver = "2.3.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
checkdepends = [
    "python-coverage",
    "python-pytest",
]
pkgdesc = "Sensible default settings for coverage"
license = "MIT"
url = "https://github.com/asottile/covdefaults"
source = f"https://github.com/asottile/covdefaults/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "adc3b7da4fb7ed00ba1daeb8de1a20580e4875983311079ee57b7544f462bae5"


def post_install(self):
    self.install_license("LICENSE")
