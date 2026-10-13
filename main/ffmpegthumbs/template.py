pkgname = "ffmpegthumbs"
pkgver = "26.08.2"
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
sha256 = "6b39041282341d583eaa90b1892b46ac70c70b24f2fdd9e782c5093ba9bac03c"
hardening = ["vis"]
