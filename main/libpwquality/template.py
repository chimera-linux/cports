pkgname = "libpwquality"
pkgver = "1.4.5"
pkgrel = 2
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--enable-pam",
    "--with-securedir=/usr/lib/security",
]
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "libtool",
    "pkgconf",
    "python-setuptools",
]
makedepends = ["cracklib-devel", "linux-pam-devel", "python-devel"]
depends = ["cracklib-words"]
pkgdesc = "Library for password quality checking"
license = "BSD-3-Clause OR GPL-2.0-or-later"
url = "https://github.com/libpwquality/libpwquality"
source = f"{url}/releases/download/libpwquality-{pkgver}/libpwquality-{pkgver}.tar.bz2"
sha256 = "6fcf18b75d305d99d04d2e42982ed5b787a081af2842220ed63287a2d6a10988"


def init_build(self):
    # see build_style/python_pep517
    self.make_build_env = {
        "PYTHON_CROSS_LIBDIR": self.profile().sysroot / "usr/lib",
        "PYTHON_CROSS_INCDIR": self.profile().sysroot
        / f"usr/include/python{self.python_version}",
    }


def post_install(self):
    self.install_license("COPYING")


@subpackage("libpwquality-devel")
def _(self):
    return self.default_devel()


@subpackage("libpwquality-python")
def _(self):
    self.subdesc = "Python bindings"
    self.depends += ["python", "cracklib-devel"]

    return ["usr/lib/python*"]
