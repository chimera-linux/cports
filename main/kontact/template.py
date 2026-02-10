pkgname = "kontact"
pkgver = "25.12.2"
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
sha256 = "18040be6e1ac53e741e5e8fee4b08c57380e088e1661fd683833b7fb1a4d3351"
