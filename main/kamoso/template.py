pkgname = "kamoso"
pkgver = "26.08.3"
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
sha256 = "624187492dd4ca1fae17d5e48681b3b3ad3bab1be92a010cd2cf74b386f8e5e9"
