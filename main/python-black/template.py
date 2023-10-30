pkgname = "python-black"
pkgver = "23.10.1"
pkgrel = 0
build_style = "python_pep517"
make_check_env = {"PYTHONPATH": "src"}
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
sha256 = "1f8ce316753428ff68749c65a5f7844631aa18c8679dfd3ca9dc1a289979c258"
# unpackaged checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
