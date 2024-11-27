pkgname = "lit"
pkgver = "18.1.8"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "cmd:FileCheck!llvm-tools",
    "cmd:not!llvm-tools",
    "python",
]
pkgdesc = "Software testing tool from LLVM"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0 WITH LLVM-exception AND NCSA"
url = "https://pypi.org/project/lit"
# the pypi source has the correct version instead of 'dev0'
source = f"$(PYPI_SITE)/l/lit/lit-{pkgver}.tar.gz"
sha256 = "47c174a186941ae830f04ded76a3444600be67d5e5fb8282c3783fba671c4edb"
# would need to run with itself (annoying)
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.TXT")
