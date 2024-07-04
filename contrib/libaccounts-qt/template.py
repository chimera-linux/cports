pkgname = "libaccounts-qt"
pkgver = "1.17"
pkgrel = 2
build_style = "makefile"
make_cmd = "gmake"
make_check_wrapper = ["dbus-run-session", "--"]
make_use_env = True
hostmakedepends = [
    "doxygen",
    "gmake",
    "pkgconf",
    "qt6-qtbase",
]
makedepends = [
    "libaccounts-glib-devel",
    "qt6-qtbase-devel",
]
checkdepends = ["dbus"]
pkgdesc = "GLib-based library for managing the accounts database"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-only"
url = "https://gitlab.com/accounts-sso/libaccounts-qt"
source = (
    f"{url}/-/archive/VERSION_{pkgver}/libaccounts-qt-VERSION_{pkgver}.tar.gz"
)
sha256 = "6ed3e976133962c1c88f6c66928ba0d0a17a570843577d31e783dc891659e5d8"
hardening = ["vis", "cfi"]


def do_configure(self):
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


def post_install(self):
    self.uninstall("usr/bin/accountstest")


@subpackage("libaccounts-qt-devel")
def _devel(self):
    return self.default_devel()
