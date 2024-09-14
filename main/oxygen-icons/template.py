pkgname = "oxygen-icons"
pkgver = "6.0.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://api.kde.org/frameworks/oxygen-icons/html"
source = f"$(KDE_SITE)/oxygen-icons/oxygen-icons-{pkgver}.tar.xz"
sha256 = "28ec182875dcc15d9278f45ced11026aa392476f1f454871b9e2c837008e5774"
