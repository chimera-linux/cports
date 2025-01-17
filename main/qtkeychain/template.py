pkgname = "qtkeychain"
pkgver = "0.15.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_WITH_QT6=ON"]
make_check_wrapper = ["dbus-run-session", "xvfb-run"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "libsecret-devel",
    "qt6-qttools-devel",
]
checkdepends = [
    "dbus",
    "xserver-xorg-xvfb",
]
pkgdesc = "Qt library for storing data in the system keychain"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/frankosterfeld/qtkeychain"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f4254dc8f0933b06d90672d683eab08ef770acd8336e44dfa030ce041dc2ca22"
hardening = ["vis", "!cfi"]
# kinda expects a graphical env and wrapper does not help
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("qtkeychain-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
