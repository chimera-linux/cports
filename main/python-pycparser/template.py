pkgname = "python-pycparser"
pkgver = "2.21"
pkgrel = 1
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
sha256 = "e644fdec12f7872f86c58ff790da456218b10f863970249516d60a5eaca77206"
# ply
options = ["brokenlinks"]


def do_check(self):
    self.do("python", "-m", "pytest")


def post_install(self):
    for f in (self.destdir / "usr/lib").glob("python3*"):
        self.rm(f / "site-packages/pycparser/ply", recursive=True)
        self.install_link(
            "../ply",
            str(f.relative_to(self.destdir) / "site-packages/pycparser/ply"),
        )
    self.install_license("LICENSE")
