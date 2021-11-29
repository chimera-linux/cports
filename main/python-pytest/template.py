pkgname = "python-pytest"
pkgver = "6.2.5"
pkgrel = 0
build_style = "python_module"
make_cmd = "gmake"
hostmakedepends = ["gmake", "python-setuptools_scm", "python-sphinx"]
depends = [
    "python-py", "python-packaging", "python-attrs", "python-pluggy",
    "python-iniconfig", "python-toml", "python-setuptools"
]
pkgdesc = "Python unit testing framework"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://docs.pytest.org/en/latest"
source = f"$(PYPI_SITE)/p/pytest/pytest-{pkgver}.tar.gz"
sha256 = "131b36680866a76e6781d13f101efb86cf674ebb9762eb70d3082b6f29889e89"
# missing checkdepends
options = ["!check"]

def post_build(self):
    from cbuild.util import make
    make.Make(self).invoke(None, ["-C", "doc/en", "man"], env = {
        "PYTHONPATH": str(self.chroot_cwd / "build/lib")
    })
    self.install_man("doc/en/_build/man/pytest.1")

def post_install(self):
    self.install_license("LICENSE")
