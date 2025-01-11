pkgname = "isoimagewriter"
pkgver = "24.12.1"
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
sha256 = "9a6bbc545b5d007be0cba9b4531e3e0a223d1f34f222ea6f3801c1dbed80b18f"
