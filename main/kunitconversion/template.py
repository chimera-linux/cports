pkgname = "kunitconversion"
pkgver = "6.13.0"
pkgrel = 0
build_style = "cmake"
# most tests require network access, pass in cbuild chroot
make_check_args = ["-E", "(category|converter|currencytableinit)test"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "ki18n-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KDE Converting physical units"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kunitconversion/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kunitconversion-{pkgver}.tar.xz"
sha256 = "208f037e8089f999e0bb0aaf85571b3a2d341cd8e40c111b35ead9d2610017ea"
hardening = ["vis"]


@subpackage("kunitconversion-devel")
def _(self):
    return self.default_devel()
