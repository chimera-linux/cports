pkgname = "kidletime"
pkgver = "6.9.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "libxscrnsaver-devel",
    "plasma-wayland-protocols",
    "qt6-qtbase-devel",
    "qt6-qtwayland-devel",
    "wayland-protocols",
]
pkgdesc = "KDE Idle time reporting of user and system"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-only"
url = "https://api.kde.org/frameworks/kidletime/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kidletime-{pkgver}.tar.xz"
sha256 = "e1665ef314660d8493f330069c477d1c8cfb0977be4b9f380d8e726b2694d242"
hardening = ["vis"]


@subpackage("kidletime-devel")
def _(self):
    return self.default_devel()
