pkgname = "python-pycparser"
pkgver = "2.22"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-ply"]
checkdepends = ["python-ply", "python-pytest"]
pkgdesc = "C99 parser in Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/eliben/pycparser"
source = f"$(PYPI_SITE)/p/pycparser/pycparser-{pkgver}.tar.gz"
sha256 = "491c8be9c040f5390f5bf44a5b07752bd07f56edf992381b05c701439eec10f6"
broken_symlinks = ["usr/lib/python3*/site-packages/pycparser/ply"]


def post_install(self):
    for f in (self.destdir / "usr/lib").glob(
        "python3*/site-packages/pycparser/ply"
    ):
        self.rm(f, recursive=True)
        f.symlink_to("../ply")
    self.install_license("LICENSE")
