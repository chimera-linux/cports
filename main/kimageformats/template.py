pkgname = "kimageformats"
pkgver = "6.11.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DKIMAGEFORMATS_HEIF=ON"]
# jpegxr; exr write fails on ppc64le
# dds; read fails on ppc64le
# avci; needs libheif built against openh264 but that SIGILLs atm
make_check_args = [
    "-E",
    "(kimageformats-read-dds|kimageformats-read-hej2|kimageformats-write-exr|kimageformats-read-avci)",
]
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
sha256 = "0c45787f97d00fc0257f7de3250d84e950de2a332c45e7528138f7cf843154cc"
