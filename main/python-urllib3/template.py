pkgname = "python-urllib3"
pkgver = "2.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-hatchling"]
depends = ["python"]
pkgdesc = "HTTP library with thread-safe connection pooling"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://urllib3.readthedocs.io"
source = f"$(PYPI_SITE)/u/urllib3/urllib3-{pkgver}.tar.gz"
sha256 = "df7aa8afb0148fa78488e7899b2c59b5f4ffcfa82e6c54ccb9dd37c1d7b52d54"
# unpackaged dependency
options = ["!check", "brokenlinks"]


def post_install(self):
    for f in (self.destdir / "usr/lib").glob(
        "python*/site-packages/urllib3/packages/six.py"
    ):
        f.unlink()
        f.symlink_to("../../six.py")

    self.install_license("LICENSE.txt")
