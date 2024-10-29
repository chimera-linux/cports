pkgname = "python-setuptools"
pkgver = "75.3.0"
pkgrel = 0
hostmakedepends = ["python-devel"]
depends = ["python", "python-wheel"]
pkgdesc = "Easily build and distribute Python packages"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pypa/setuptools"
source = f"$(PYPI_SITE)/s/setuptools/setuptools-{pkgver}.tar.gz"
sha256 = "fba5dd4d766e97be1b1681d98712680ae8f2f26d7881245f2ce9e40714f1a686"
env = {
    "SETUPTOOLS_INSTALL_WINDOWS_SPECIFIC_FILES": "0",
    "SETUPTOOLS_DISABLE_VERSIONED_EASY_INSTALL_SCRIPT": "1",
}
# missing checkdepends
options = ["!check"]


def build(self):
    self.do(
        "python3",
        "setup.py",
        "build",
    )


def install(self):
    from cbuild.util import python

    self.do(
        "python3",
        "setup.py",
        "install",
        "--prefix=/usr",
        "--root=" + str(self.chroot_destdir),
    )
    python.precompile(self, "usr/lib")


def post_install(self):
    self.install_license("LICENSE")
    self.uninstall(
        "usr/lib/python*/site-packages/setuptools/*/tests", glob=True
    )
    self.uninstall(
        "usr/lib/python*/site-packages/setuptools/_vendor/*/tests", glob=True
    )
    self.uninstall("usr/lib/python*/site-packages/setuptools/tests", glob=True)
    self.uninstall(
        "usr/lib/python*/site-packages/setuptools/_vendor/wheel*", glob=True
    )
