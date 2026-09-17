pkgname = "kio-gdrive"
pkgver = "26.08.1"
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
    "kaccounts-integration-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kio-devel",
    "knotifications-devel",
    "libkgapi-devel",
    "purpose-devel",
    "qt6-qtbase-devel",
    "qtkeychain-devel",
]
pkgdesc = "KDE KIO plugin for Google Drive"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kio_gdrive"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kio-gdrive-{pkgver}.tar.xz"
sha256 = "ce1a91277edf256e9fc6a90fbc486dabd951b329c81d1c9328b0fa3bf06474c8"
