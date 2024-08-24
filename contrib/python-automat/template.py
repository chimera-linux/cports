pkgname = "python-automat"
pkgver = "24.8.1"
pkgrel = 0
build_style = "python_pep517"
make_build_env = {"SETUPTOOLS_SCM_PRETEND_VERSION": pkgver}
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Finite state machines for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/glyph/Automat"
source = f"$(PYPI_SITE)/A/Automat/automat-{pkgver}.tar.gz"
sha256 = "b34227cf63f6325b8ad2399ede780675083e439b20c323d376373d8ee6306d88"


def do_check(self):
    self.do("pytest", "src/automat/_test")


def post_install(self):
    self.install_license("LICENSE")
