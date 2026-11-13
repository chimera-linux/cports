pkgname = "svgpart"
pkgver = "26.08.3"
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
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kparts-devel",
    "kxmlgui-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
]
pkgdesc = "KParts plugin for SVG"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/svgpart"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/svgpart-{pkgver}.tar.xz"
sha256 = "42d9a4d9833b9428e693c074493844006f83b1b48e6d3f2c3fb42ba55bc8b31d"
hardening = ["vis"]
