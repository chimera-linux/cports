pkgname = "ffmpegthumbs"
pkgver = "25.12.2"
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
sha256 = "18059809baa8d2525b20988f9176d010ae8758703917c6cafd8199be965bc446"
hardening = ["vis"]
