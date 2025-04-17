pkgname = "svgpart"
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
sha256 = "539f725720599ca67d507f3c4e07524ac8192325f173b3449f83098bd4aaa652"
hardening = ["vis"]
