pkgname = "oxygen-icons"
pkgver = "6.1.0"
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
sha256 = "16ca971079c5067c4507cabf1b619dc87dd6b326fd5c2dd9f5d43810f2174d68"
