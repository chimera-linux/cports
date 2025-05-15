pkgname = "kcalendarcore"
pkgver = "6.14.0"
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
sha256 = "702bfc2edfced4d0903365657434fd8c2dc0b8f66d0ce96e4ea0b6950ef8798b"
# a ton of failures due to different sort order and whatnot
options = ["!check"]


@subpackage("kcalendarcore-devel")
def _(self):
    return self.default_devel()
