pkgname = "signon-ui"
# last release is from previous century
pkgver = "0.17_git20231016"
pkgrel = 1
_gitrev = "eef943f0edf3beee8ecb85d4a9dae3656002fc24"
build_style = "makefile"
make_use_env = True
hostmakedepends = [
    "pkgconf",
    "qt6-qtbase",
]
makedepends = [
    "libaccounts-qt-devel",
    "libnotify-devel",
    "libproxy-devel",
    "qt6-qtwebengine-devel",
    "signond-devel",
]
checkdepends = ["dbus-test-runner", "xserver-xorg-xvfb"]
pkgdesc = "Qt UI for signond"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-only"
url = "https://gitlab.com/accounts-sso/signon-ui"
source = f"{url}/-/archive/{_gitrev}.tar.gz"
sha256 = "0906a1adee88e331e9dcf1f2d5978c24f8564fb734f5c114c88bddb63196d3d4"


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
