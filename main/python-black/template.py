pkgname = "python-black"
pkgver = "23.9.1"
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
] + list(depends)
pkgdesc = "Python formatting tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://black.readthedocs.io"
source = f"$(PYPI_SITE)/b/black/black-{pkgver}.tar.gz"
sha256 = "24b6b3ff5c6d9ea08a8888f6977eae858e1f340d7260cf56d70a49823236b62d"
# unpackaged checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
