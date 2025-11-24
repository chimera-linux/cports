pkgname = "kidletime"
pkgver = "6.20.0"
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
sha256 = "ecbcac5e062a27d3161747d6bf49dd603281a378d26c048915e762ab194540d9"
hardening = ["vis"]


@subpackage("kidletime-devel")
def _(self):
    return self.default_devel()
