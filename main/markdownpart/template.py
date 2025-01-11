pkgname = "markdownpart"
pkgver = "24.12.1"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://apps.kde.org/markdownpart"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/markdownpart-{pkgver}.tar.xz"
)
sha256 = "563e70dcf5ac857309f675ae6cce2403a8b6daa1f5711a9ffebcf4748e2f458b"
hardening = ["vis"]
