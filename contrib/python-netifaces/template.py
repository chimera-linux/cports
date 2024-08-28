pkgname = "python-netifaces"
pkgver = "0.11.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
makedepends = ["linux-headers", "python-devel"]
pkgdesc = "Module to access network interface information"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://alastairs-place.net/projects/netifaces"
source = f"$(PYPI_SITE)/n/netifaces/netifaces-{pkgver}.tar.gz"
sha256 = "043a79146eb2907edf439899f262b3dfe41717d34124298ed281139a8b93ca32"
# does not use pytest and is not useful inside chroot
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
