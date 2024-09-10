pkgname = "milou"
pkgver = "6.1.5"
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
sha256 = "405148a12ee7fec89388f99bc5485507548c8512de22ba03025154442735390a"
hardening = ["vis"]
