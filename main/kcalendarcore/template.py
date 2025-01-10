pkgname = "kcalendarcore"
pkgver = "6.10.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/frameworks/kcalendarcore/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kcalendarcore-{pkgver}.tar.xz"
sha256 = "988f2fd648341967384d95d3d12bb936a8a7737a931e72c2b5616050bc30336a"
# a ton of failures due to different sort order and whatnot
options = ["!check"]


@subpackage("kcalendarcore-devel")
def _(self):
    return self.default_devel()
