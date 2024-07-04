pkgname = "isoimagewriter"
pkgver = "24.05.2"
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
sha256 = "c725e097f065a5ef721060c2df2d3e351a60429f52d086e37a7ee73d036792d5"
