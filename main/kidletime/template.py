pkgname = "kidletime"
pkgver = "6.18.0"
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
sha256 = "44afc88543b23c519eb5f55e7c5120ccd6d4eb2eaaa5bee24e3fb5e4a695dab7"
hardening = ["vis"]


@subpackage("kidletime-devel")
def _(self):
    return self.default_devel()
