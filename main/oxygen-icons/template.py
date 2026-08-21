pkgname = "oxygen-icons"
pkgver = "6.29.0"
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
sha256 = "3d365f052087de1b5f870a4ecee083a6eb6e5f9174925152331110025113367a"
