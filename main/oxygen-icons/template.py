pkgname = "oxygen-icons"
pkgver = "6.27.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "qt6-qtbase-devel",
]
checkdepends = [
    "fdupes",
]
pkgdesc = "Oxygen icon themes"
license = "GPL-2.0-or-later"
url = "https://api.kde.org/frameworks/oxygen-icons/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/oxygen-icons-{pkgver}.tar.xz"
sha256 = "f36a0884e6b9e554721c0f8cbd40c20ed4ff1a1b7d7e293c67d3d11d0b72cf9a"
