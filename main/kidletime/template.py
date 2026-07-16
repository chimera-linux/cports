pkgname = "kidletime"
pkgver = "6.28.0"
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
sha256 = "0ada459a4ccdf75d17329bfa4ee42c2c6e7b3ead1ec4b427f82bed063b970ff5"
hardening = ["vis"]


@subpackage("kidletime-devel")
def _(self):
    return self.default_devel()
