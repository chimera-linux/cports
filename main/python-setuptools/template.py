pkgname = "python-setuptools"
pkgver = "78.1.0"
pkgrel = 0
hostmakedepends = ["python-devel"]
depends = ["python", "python-wheel"]
pkgdesc = "Easily build and distribute Python packages"
license = "MIT"
url = "https://github.com/pypa/setuptools"
source = f"$(PYPI_SITE)/s/setuptools/setuptools-{pkgver}.tar.gz"
sha256 = "18fd474d4a82a5f83dac888df697af65afa82dec7323d09c3e37d1f14288da54"
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
    self.uninstall("usr/lib/python*/site-packages/setuptools/tests", glob=True)
    self.uninstall(
        "usr/lib/python*/site-packages/setuptools/_vendor/wheel*", glob=True
    )
