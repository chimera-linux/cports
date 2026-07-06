pkgname = "ffmpegthumbs"
pkgver = "26.04.3"
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
sha256 = "a6d7a12a57f24113789203413d40a4355ce4c0aff516384ecd2c548ce42f389b"
hardening = ["vis"]
