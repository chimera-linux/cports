pkgname = "kpty"
pkgver = "6.14.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "kcoreaddons-devel",
    "ki18n-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KDE Interface to pseudo terminal devices"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kpty/html"
source = (
    f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kpty-{pkgver}.tar.xz"
)
sha256 = "979e0bb19cd7d9db843bf5df35115447eb492637a099eb53c345b82fc80bea65"
hardening = ["vis"]


@subpackage("kpty-devel")
def _(self):
    return self.default_devel()
