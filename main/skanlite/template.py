pkgname = "skanlite"
pkgver = "24.12.3"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DQT_MAJOR_VERSION=6"]
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
sha256 = "45de753338ba358d3298af0b89e1c1f089c0096c3748f3fbe1050c43baf55834"
