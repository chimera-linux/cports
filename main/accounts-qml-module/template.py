pkgname = "accounts-qml-module"
# last release from previous century
pkgver = "0.7_git20231028"
pkgrel = 1
_gitrev = "05e79ebbbf3784a87f72b7be571070125c10dfe3"
build_style = "makefile"
make_use_env = True
hostmakedepends = [
    "pkgconf",
    "qt6-qtbase",
]
makedepends = [
    "libaccounts-qt-devel",
    "qt6-qtdeclarative-devel",
    "signond-devel",
]
checkdepends = ["dbus-test-runner", "xwayland-run"]
pkgdesc = "QML bindings for signond/libaccounts-qt"
license = "LGPL-2.1-only"
url = "https://gitlab.com/accounts-sso/accounts-qml-module"
source = f"{url}/-/archive/{_gitrev}.tar.gz"
sha256 = "1a53a6d8a3a56694244bc24bdab844d91420483744822d08ae8517ff7df84763"


def configure(self):
    # TODO: build style these
    self.do(
        "qmake6",
        "PREFIX=/usr",
        "CONFIG+=no_docs",
        f"QMAKE_CFLAGS={self.get_cflags(shell=True)}",
        f"QMAKE_CXXFLAGS={self.get_cxxflags(shell=True)}",
        f"QMAKE_LFLAGS={self.get_ldflags(shell=True)}",
    )


def init_install(self):
    self.make_install_args += [f"INSTALL_ROOT={self.chroot_destdir}"]


def post_install(self):
    # mistakenly installed
    self.uninstall("usr/bin/tst_plugin")
