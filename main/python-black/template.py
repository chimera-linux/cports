pkgname = "python-black"
pkgver = "23.7.0"
pkgrel = 0
build_style = "python_pep517"
make_check_env = {"PYTHONPATH": "src"}
hostmakedepends = ["python-build", "python-installer", "python-hatch_vcs"]
depends = [
    "python-click",
    "python-platformdirs",
    "python-pathspec",
    "python-packaging",
    "python-mypy_extensions",
]
checkdepends = [
    "python-pytest",
    "python-pytest-xdist",
    "python-aiohttp",
    "python-ipython",
    "python-tokenize_rt",
] + depends
pkgdesc = "Python formatting tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://black.readthedocs.io"
source = f"$(PYPI_SITE)/b/black/black-{pkgver}.tar.gz"
sha256 = "022a582720b0d9480ed82576c920a8c1dde97cc38ff11d8d8859b3bd6ca9eedb"
# unpackaged checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
