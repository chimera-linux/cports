pkgname = "python-urllib3"
pkgver = "1.26.6"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python-six"]
pkgdesc = "HTTP library with thread-safe connection pooling"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://urllib3.readthedocs.io"
source = f"$(PYPI_SITE)/u/urllib3/urllib3-{pkgver}.tar.gz"
sha256 = "f57b4c16c62fa2760b7e3d97c35b255512fb6b59a259730f36ba32ce9f8e342f"
# unpackaged dependency
options = ["!check", "brokenlinks"]

def post_install(self):
    for f in (self.destdir / "usr/lib").glob(
        "python*/site-packages/urllib3/packages/six.py"
    ):
        f.unlink()
        f.symlink_to("../../six.py")

    self.install_license("LICENSE.txt")
