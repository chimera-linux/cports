pkgname = "milou"
pkgver = "6.2.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "kconfig-devel",
    "ki18n-devel",
    "krunner-devel",
    "ksvg-devel",
    "kwindowsystem-devel",
    "libplasma-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE Dedicated search application"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://api.kde.org/plasma/milou/html"
source = f"$(KDE_SITE)/plasma/{pkgver}/milou-{pkgver}.tar.xz"
sha256 = "b1f1b4e13fb40476531b3a63e766a23ef7794de1b8620242b4c51ab445f9b1c5"
hardening = ["vis"]
