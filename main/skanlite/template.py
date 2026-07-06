pkgname = "skanlite"
pkgver = "26.04.3"
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
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kio-devel",
    "kxmlgui-devel",
    "libksane-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE scanning application for images"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://apps.kde.org/skanlite"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/skanlite-{pkgver}.tar.xz"
sha256 = "dac757451b430192a00eef7a90aad14f5e59d9460e9ff5fb162922ca47403417"
