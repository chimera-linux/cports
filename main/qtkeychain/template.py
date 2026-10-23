pkgname = "qtkeychain"
pkgver = "0.17.0"
pkgrel = 0
build_style = "cmake"
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
sha256 = "3b85c3929034b0a99da777130c34d99f006fcd3a9d56564159399a33fee0e504"
hardening = ["vis", "!cfi"]
# kinda expects a graphical env and wrapper does not help
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("qtkeychain-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
