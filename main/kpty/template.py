pkgname = "kpty"
pkgver = "6.12.0"
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
sha256 = "84e713ccf630c91a351ccae3d95c3b857b67e446fc491a62a013dc10194f803a"
hardening = ["vis"]


@subpackage("kpty-devel")
def _(self):
    return self.default_devel()
