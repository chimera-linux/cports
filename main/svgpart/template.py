pkgname = "svgpart"
pkgver = "24.12.2"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/svgpart"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/svgpart-{pkgver}.tar.xz"
sha256 = "738e23fe94cc223b9a1767f416a1acb43b364fcd71fb420d2217853f0c665f9d"
hardening = ["vis"]
