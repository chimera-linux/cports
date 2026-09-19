pkgname = "python-tokenize-rt"
pkgver = "6.2.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
checkdepends = ["python-pytest"]
pkgdesc = "Wrapper around the stdlib tokenize which roundtrips"
license = "MIT"
url = "https://github.com/asottile/tokenize-rt"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "31bb2c9c5a954cb6c29d60218f83ea07be08faac5e2f4431d0463f9adb63fb6e"


def post_install(self):
    self.install_license("LICENSE")
