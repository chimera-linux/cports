pkgname = "python-urllib3"
pkgver = "1.26.7"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python-six"]
pkgdesc = "HTTP library with thread-safe connection pooling"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://urllib3.readthedocs.io"
source = f"$(PYPI_SITE)/u/urllib3/urllib3-{pkgver}.tar.gz"
sha256 = "4987c65554f7a2dbf30c18fd48778ef124af6fab771a377103da0585e2336ece"
# unpackaged dependency
options = ["!check", "brokenlinks"]

def post_install(self):
    for f in (self.destdir / "usr/lib").glob(
        "python*/site-packages/urllib3/packages/six.py"
    ):
        f.unlink()
        f.symlink_to("../../six.py")

    self.install_license("LICENSE.txt")
