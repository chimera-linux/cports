pkgname = "kimageformats"
pkgver = "6.19.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DKIMAGEFORMATS_HEIF=ON"]
# jpegxr; exr write fails on ppc64le
# dds; read fails on ppc64le
# xcf; read fails on aarch64
# avci; needs libheif built against openh264 but that SIGILLs atm
make_check_args = [
    "-E",
    "kimageformats-(write-exr|read-(dds|hej2|xcf|avci))",
]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja", "pkgconf"]
makedepends = [
    "karchive-devel",
    "libavif-devel",
    "libheif-devel",
    "libjxl-devel",
    "libraw-devel",
    "openexr-devel",
    "openjpeg-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "Image format plugins for Qt6"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kimageformats/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kimageformats-{pkgver}.tar.xz"
sha256 = "fc825326aa6b8c1321947ff523d3d006eef4c65fde40f379c6900d06967fae1c"
