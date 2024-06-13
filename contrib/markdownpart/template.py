pkgname = "markdownpart"
pkgver = "24.05.1"
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
sha256 = "793838adc6d5563cbd14e637b210e76d7f28f233c75dbdf092c6219d2fdc0de1"
# CFI: check
hardening = ["vis", "!cfi"]
