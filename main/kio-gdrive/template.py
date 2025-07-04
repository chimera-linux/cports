pkgname = "kio-gdrive"
pkgver = "25.04.3"
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
sha256 = "a927c8e98907e6e83e0d6761b26cdd5c25ce48605fcc3a5cbc2c1a8b3bfa1b22"
