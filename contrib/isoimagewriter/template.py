pkgname = "isoimagewriter"
pkgver = "24.05.1"
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
sha256 = "aed0ee7744a14e8ba9dc9694c8a94f3fe0e18f3ec409346a1faf3d62f078287c"
