pkgname = "kamoso"
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
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "kconfig-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kio-devel",
    "kirigami-devel",
    "knotifications-devel",
    "purpose-devel",
    "qt6-qtbase-devel",
    "qt6-qtdeclarative-devel",
]
depends = ["gst-plugins-good", "gst-plugins-good-qt6"]
pkgdesc = "KDE camera app"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kamoso"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kamoso-{pkgver}.tar.xz"
sha256 = "c26e7d00bd15eedbaa252694cf9c991d7995bfd2ddd2c39a9cf19be73a6ded1f"
