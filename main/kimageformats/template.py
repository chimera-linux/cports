pkgname = "kimageformats"
pkgver = "6.9.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DKIMAGEFORMATS_HEIF=ON"]
# jpegxr; exr write fails on ppc64le
make_check_args = ["-E", "(kimageformats-read-hej2|kimageformats-write-exr)"]
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
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kimageformats-{pkgver}.tar.xz"
sha256 = "8317dce66a773648c5c00f0a676156c4ee4e71d7c98540900c31b7b70a50f6df"
