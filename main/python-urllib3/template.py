pkgname = "python-urllib3"
pkgver = "1.26.12"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python", "python-six"]
pkgdesc = "HTTP library with thread-safe connection pooling"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://urllib3.readthedocs.io"
source = f"$(PYPI_SITE)/u/urllib3/urllib3-{pkgver}.tar.gz"
sha256 = "3fa96cf423e6987997fc326ae8df396db2a8b7c667747d47ddd8ecba91f4a74e"
# unpackaged dependency
options = ["!check", "brokenlinks"]

def post_install(self):
    for f in (self.destdir / "usr/lib").glob(
        "python*/site-packages/urllib3/packages/six.py"
    ):
        f.unlink()
        f.symlink_to("../../six.py")

    self.install_license("LICENSE.txt")

# FIXME visibility
hardening = ["!vis"]
