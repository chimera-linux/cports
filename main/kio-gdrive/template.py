pkgname = "kio-gdrive"
pkgver = "25.04.2"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DQT_MAJOR_VERSION=6"]
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
sha256 = "6a73522ba1fe8224efeb8adc6a5b2902d55928706e5520ad4b4a3bbb4f114cf0"
