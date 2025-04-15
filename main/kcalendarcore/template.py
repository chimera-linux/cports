pkgname = "kcalendarcore"
pkgver = "6.13.0"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "libical-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = [
    "perl",
    "xwayland-run",
]
pkgdesc = "KDE calendar access library"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/frameworks/kcalendarcore/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kcalendarcore-{pkgver}.tar.xz"
sha256 = "e1504a851f39fbf9beac05d622ca46ebbd6e9f2b1106e71c5d4bbf7ca7fa1f41"
# a ton of failures due to different sort order and whatnot
options = ["!check"]


@subpackage("kcalendarcore-devel")
def _(self):
    return self.default_devel()
