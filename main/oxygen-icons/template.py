pkgname = "oxygen-icons"
pkgver = "6.30.0"
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
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/oxygen-icons-{pkgver}.tar.xz"
sha256 = "8ae13c8827883d54cf903f63fbc9eff246b3a4dd8c0d7c835b610d642f49f37e"
