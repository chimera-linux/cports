pkgname = "python-jsonpatch"
pkgver = "1.33"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-jsonpointer"]
pkgdesc = "Apply JSON patches"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/stefankoegl/python-json-patch"
source = f"$(PYPI_SITE)/j/jsonpatch/jsonpatch-{pkgver}.tar.gz"
sha256 = "9fcd4009c41e6d12348b4a0ff2563ba56a2923a7dfee731d004e212e1ee5030c"
# does not use pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
