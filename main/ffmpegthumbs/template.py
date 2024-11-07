pkgname = "ffmpegthumbs"
pkgver = "24.08.3"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/ffmpegthumbs"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/ffmpegthumbs-{pkgver}.tar.xz"
)
sha256 = "1945360c68e6738828b7130f0d7b5b64ea129edd581bbebf665296e4a9c3cac4"
hardening = ["vis"]
