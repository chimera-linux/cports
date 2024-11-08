pkgname = "kimageformats"
pkgver = "6.8.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DKIMAGEFORMATS_HEIF=ON"]
# jpegxr
make_check_args = ["-E", "kimageformats-read-hej2"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "karchive-devel",
    "libavif-devel",
    "openexr-devel",
    "libjxl-devel",
    "libheif-devel",
    "libraw-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "Image format plugins for Qt6"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kimageformats/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kimageformats-{pkgver}.tar.xz"
sha256 = "d9f262641cc47e5f2dd1bdd56ee92e379ab4cb34d460dfc884fd991250d7b417"
