pkgname = "lxqt-globalkeys"
pkgver = "2.5.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "lxqt-build-tools",
    "ninja",
    "perl",
    "pkgconf",
]
makedepends = [
    "kwindowsystem-devel",
    "liblxqt-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Daemon used to register global keyboard shortcuts"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-globalkeys"
source = f"{url}/releases/download/{pkgver}/lxqt-globalkeys-{pkgver}.tar.xz"
sha256 = "9f02427103526d24c4eb1e1dd2199421b76f2c8a6705e037232a5a6f49a2316b"
options = ["etcfiles"]


@split("devel")
def _(self):
    return self.default_devel()
