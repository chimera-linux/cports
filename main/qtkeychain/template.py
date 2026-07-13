pkgname = "qtkeychain"
pkgver = "0.16.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_WITH_QT6=ON"]
make_check_wrapper = ["dbus-run-session", "--", "wlheadless-run", "--"]
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
    "xwayland-run",
]
pkgdesc = "Qt library for storing data in the system keychain"
license = "BSD-3-Clause"
url = "https://github.com/frankosterfeld/qtkeychain"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "3be26ec4ae30eecf0c2ff7572ba83799791b157c76e15a05ef35f23dc25e4054"
hardening = ["vis", "!cfi"]
# kinda expects a graphical env and wrapper does not help
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("qtkeychain-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
