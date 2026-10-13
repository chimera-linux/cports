pkgname = "skanlite"
pkgver = "26.08.2"
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
sha256 = "57789835a9bc488e7e8b204e77a636cf5316659229427e357654c85c221df5c2"
