pkgname = "ffmpegthumbs"
pkgver = "26.08.3"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_WITH_QT6=ON"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "ffmpeg-devel",
    "kconfig-devel",
    "kio-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KDE thumbnail creator"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/ffmpegthumbs"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/ffmpegthumbs-{pkgver}.tar.xz"
)
sha256 = "e55a6db0c4582648a6912fb2eebbd5a8cc60e6ef50a90dac03c75e7e69eb6347"
hardening = ["vis"]
