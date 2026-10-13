pkgname = "oxygen-icons"
pkgver = "6.31.0"
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
sha256 = "f63811206c7c01b78c625abfbe866484b71849be833272a7375bb9f86ac7d5b5"
