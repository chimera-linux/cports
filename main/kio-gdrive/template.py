pkgname = "kio-gdrive"
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
sha256 = "8ddc32d39f79bbb607a6d134ac5aa1e08627fee7523339d2dc9eee2b81e5a7d4"
