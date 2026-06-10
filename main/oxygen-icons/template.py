pkgname = "oxygen-icons"
pkgver = "6.2.0"
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
source = f"$(KDE_SITE)/oxygen-icons/oxygen-icons-{pkgver}.tar.xz"
sha256 = "61fd2ef56e7afbbbab034052017264ad00d074c7be06f0855d4c805a5cbacfdd"
