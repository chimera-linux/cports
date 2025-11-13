pkgname = "svgpart"
pkgver = "25.08.3"
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
sha256 = "97f6fdb4ff3110e41d8df6b25f0d184f5235d889d8c7c15c7c6bbb1a2f06de17"
hardening = ["vis"]
