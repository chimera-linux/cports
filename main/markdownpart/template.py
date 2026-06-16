pkgname = "markdownpart"
pkgver = "26.04.2"
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
sha256 = "094c4c97c5e60ef9e91ccb49a9926a5c84cc9dafd6da33bec833f1dd9695deba"
hardening = ["vis"]
