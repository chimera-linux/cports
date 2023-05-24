pkgname = "python-tomli"
pkgver = "2.0.1"
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
_flit_version = "3.6.0"
source = [
    f"$(PYPI_SITE)/t/tomli/tomli-{pkgver}.tar.gz",
    f"$(PYPI_SITE)/f/flit_core/flit_core-{_flit_version}.tar.gz",
]
sha256 = [
    "de526c12914f0c550d15924c62d72abc48d6fe7364aa87328337a31007fe8a4f",
    "5892962ab8b8ea945835b3a288fe9dd69316f1903d5288c3f5cafdcdd04756ad",
]
# no tests in archive
options = ["!check"]


def init_build(self):
    # tomli requires importing itself and flit_core to build
    fpath = self.chroot_builddir / self.wrksrc / f"flit_core-{_flit_version}"
    self.make_build_env = {"PYTHONPATH": f"{self.chroot_cwd}:{fpath}"}


def post_install(self):
    self.install_license("LICENSE")
