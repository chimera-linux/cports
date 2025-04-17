pkgname = "kontact"
pkgver = "25.04.0"
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
    "grantleetheme-devel",
    "kcmutils-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kontactinterface-devel",
    "libkdepim-devel",
    "pimcommon-devel",
    "qt6-qtbase-devel",
    "qt6-qtwebengine-devel",
]
pkgdesc = "KDE PIM unified UI"
license = "LGPL-2.0-only AND GPL-2.0-or-later"
url = "https://kontact.kde.org"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kontact-{pkgver}.tar.xz"
sha256 = "3eb5c3beac967aa4246078fab93c45bba6eb9ab838349d8a87b6d660265409e9"
