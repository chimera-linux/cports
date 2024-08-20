pkgname = "python-vdf"
pkgver = "3.4"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
checkdepends = ["python-pytest"]
pkgdesc = "Serialization module for Valve's key/value format"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MIT"
url = "https://github.com/ValvePython/vdf"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c9fb42b6de9daf475cd229377d0c32d6e87c0f21e874a35e0e679eb201723a67"


def post_install(self):
    self.install_license("LICENSE")
