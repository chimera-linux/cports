pkgname = "python-idna"
pkgver = "3.3"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python"]
pkgdesc = "Internationalized Domain Names in Applications (IDNA) for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/kjd/idna"
source = f"$(PYPI_SITE)/i/idna/idna-{pkgver}.tar.gz"
sha256 = "9d643ff0a55b762d5cdb124b8eaa99c66322e2157b69160bc32796e824360e6d"
options = ["lto"]

def post_install(self):
    self.install_license("LICENSE.md")
