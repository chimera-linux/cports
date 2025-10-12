pkgname = "kidletime"
pkgver = "6.19.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja", "pkgconf"]
makedepends = [
    "libxscrnsaver-devel",
    "plasma-wayland-protocols",
    "qt6-qttools-devel",
    "qt6-qtwayland-devel",
    "wayland-protocols",
]
pkgdesc = "KDE Idle time reporting of user and system"
license = "LGPL-2.0-only"
url = "https://api.kde.org/frameworks/kidletime/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kidletime-{pkgver}.tar.xz"
sha256 = "df82c386fef8dc98ea5976ffef1da11539c1914d21b773ce62f4533b5ad16f65"
hardening = ["vis"]


@subpackage("kidletime-devel")
def _(self):
    return self.default_devel()
