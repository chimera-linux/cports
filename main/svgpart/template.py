pkgname = "svgpart"
pkgver = "24.08.2"
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
sha256 = "ca6151fca6240c52f431bcc98ffe4e16492efee188d7a2312f06db65c0b5c618"
hardening = ["vis"]
