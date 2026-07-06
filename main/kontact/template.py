pkgname = "kontact"
pkgver = "26.04.3"
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
sha256 = "28efd897d46825e9ab66b050a8076663d6a74a286fd4a1f8183fc12695b2f4d5"
