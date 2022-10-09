pkgname = "python-pytest"
pkgver = "7.1.3"
pkgrel = 0
build_style = "python_module"
make_cmd = "gmake"
hostmakedepends = [
    "gmake", "python-setuptools_scm", "python-sphinx", "python-attrs",
    "python-iniconfig", "python-py", "python-pluggy", "python-wheel",
]
depends = [
    "python-packaging", "python-tomli", "python-attrs", "python-iniconfig",
    "python-py", "python-pluggy",
]
pkgdesc = "Python unit testing framework"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://docs.pytest.org/en/latest"
source = f"$(PYPI_SITE)/p/pytest/pytest-{pkgver}.tar.gz"
sha256 = "4f365fec2dff9c1162f834d9f18af1ba13062db0c708bf7b946f8a5c76180c39"
# missing checkdepends
options = ["!check"]

def post_build(self):
    from cbuild.util import make
    make.Make(self).invoke(None, ["-C", "doc/en", "man"], env = {
        "PYTHONPATH": str(self.chroot_cwd / "build/lib")
    })

def post_install(self):
    self.install_man("doc/en/_build/man/pytest.1")
    self.install_license("LICENSE")
