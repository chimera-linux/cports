pkgname = "isoimagewriter"
pkgver = "25.08.0"
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
license = "GPL-3.0-only"
url = "https://apps.kde.org/isoimagewriter"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/isoimagewriter-{pkgver}.tar.xz"
)
sha256 = "1cdafe7d404b2ba7a00901f6e860a23a7172ac997774c8a7d0b696edfcc5e4e0"
