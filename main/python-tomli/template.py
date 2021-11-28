pkgname = "python-tomli"
pkgver = "1.2.2"
pkgrel = 0
build_wrksrc = f"tomli-{pkgver}"
build_style = "python_pep517"
hostmakedepends = ["python-pip"]
depends = ["python"]
pkgdesc = "TOML parser for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/hukkin/tomli"
# dependency cycle, so we need to download our own flit_core:
#  https://github.com/hukkin/tomli/issues/130
#  https://github.com/takluyver/flit/issues/451
_flit_version = "3.4.0"
source = [
    f"$(PYPI_SITE)/t/tomli/tomli-{pkgver}.tar.gz",
    f"$(PYPI_SITE)/f/flit_core/flit_core-{_flit_version}.tar.gz",
]
sha256 = [
    "c6ce0015eb38820eaf32b5db832dbc26deb3dd427bd5f6556cf0acac2c214fee",
    "29468fa2330969167d1f5c23eb9c0661cb6dacfcd46f361a274609a7f4197530"
]
# no tests in archive
options = ["!check", "lto"]

def init_build(self):
    # tomli requires importing itself and flit_core to build
    fpath = self.chroot_builddir / self.wrksrc / f"flit_core-{_flit_version}"
    self.make_build_env = {
        "PYTHONPATH": f"{self.chroot_cwd}:{fpath}"
    }

def post_install(self):
    self.install_license("LICENSE")
