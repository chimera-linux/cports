pkgname = "python-black"
pkgver = "23.3.0"
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
sha256 = "1c7b8d606e728a41ea1ccbd7264677e494e87cf630e399262ced92d4a8dac940"
# unpackaged checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
