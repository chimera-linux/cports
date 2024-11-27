pkgname = "signond"
pkgver = "8.61"
pkgrel = 1
build_style = "makefile"
make_use_env = True
hostmakedepends = [
    "doxygen",
    "pkgconf",
    "qt6-qtbase",
]
makedepends = ["qt6-qtbase-devel"]
checkdepends = ["dbus-x11"]
pkgdesc = "D-Bus service for user authentication"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://gitlab.com/accounts-sso/signond"
source = f"{url}/-/archive/VERSION_{pkgver}/signond-VERSION_{pkgver}.tar.gz"
sha256 = "3dd57c25e1bf1583b2cb857f96831e38e73d40264ff66ca43e63bb7233f76828"


def configure(self):
    # TODO: build style these
    self.do(
        "qmake6",
        "PREFIX=/usr",
        f"QMAKE_CFLAGS={self.get_cflags(shell=True)}",
        f"QMAKE_CXXFLAGS={self.get_cxxflags(shell=True)}",
        f"QMAKE_LFLAGS={self.get_ldflags(shell=True)}",
    )


def init_install(self):
    self.make_install_args += [f"INSTALL_ROOT={self.chroot_destdir}"]


@subpackage("signond-devel")
def _(self):
    return self.default_devel()
