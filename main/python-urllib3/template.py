pkgname = "python-urllib3"
pkgver = "2.0.7"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-hatchling"]
depends = ["python", "python-six"]
pkgdesc = "HTTP library with thread-safe connection pooling"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://urllib3.readthedocs.io"
source = f"$(PYPI_SITE)/u/urllib3/urllib3-{pkgver}.tar.gz"
sha256 = "c97dfde1f7bd43a71c8d2a58e369e9b2bf692d1334ea9f9cae55add7d0dd0f84"
# unpackaged dependency
options = ["!check", "brokenlinks"]


def post_install(self):
    for f in (self.destdir / "usr/lib").glob(
        "python*/site-packages/urllib3/packages/six.py"
    ):
        f.unlink()
        f.symlink_to("../../six.py")

    self.install_license("LICENSE.txt")
