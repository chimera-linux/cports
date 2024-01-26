pkgname = "python-black"
pkgver = "24.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-hatch_vcs"]
depends = [
    "python-click",
    "python-mypy_extensions",
    "python-packaging",
    "python-pathspec",
    "python-platformdirs",
]
checkdepends = [
    "python-aiohttp",
    "python-ipython",
    "python-pytest",
    "python-pytest-xdist",
    "python-tokenize_rt",
] + depends
pkgdesc = "Python formatting tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://black.readthedocs.io"
source = f"$(PYPI_SITE)/b/black/black-{pkgver}.tar.gz"
sha256 = "30fbf768cd4f4576598b1db0202413fafea9a227ef808d1a12230c643cefe9fc"
# unpackaged checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
