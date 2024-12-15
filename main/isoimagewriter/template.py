pkgname = "isoimagewriter"
pkgver = "24.12.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "gpgme-qt-devel",
    "karchive-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kwidgetsaddons-devel",
    "qt6-qtbase-devel",
    "solid-devel",
]
pkgdesc = "KDE ISO USB writer"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-only"
url = "https://apps.kde.org/isoimagewriter"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/isoimagewriter-{pkgver}.tar.xz"
)
sha256 = "8b1687e963666e1de8f8cea647702cc168d6632e9361d4062e5b16faa7a64c64"
