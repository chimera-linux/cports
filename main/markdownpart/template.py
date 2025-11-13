pkgname = "markdownpart"
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
    "ki18n-devel",
    "kparts-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KParts plugin for Markdown"
license = "LGPL-2.1-or-later"
url = "https://apps.kde.org/markdownpart"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/markdownpart-{pkgver}.tar.xz"
)
sha256 = "59524b2377bed096234a8b471f3c1754553d1d3f12239deb377c9c02d543653d"
hardening = ["vis"]
