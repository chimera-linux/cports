pkgname = "skanlite"
pkgver = "25.08.1"
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
sha256 = "8bece39f2d7eab4f9fb8aeaeefbd630c2ae7ce25bb6b63fa8f4f15d23dfd9c6c"
