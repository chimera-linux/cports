pkgname = "markdownpart"
pkgver = "26.08.1"
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
sha256 = "2c3ff564fe78d0dae80ae45875cccb1afe8da56045b9a0c2c47d13b29a5a6827"
hardening = ["vis"]
