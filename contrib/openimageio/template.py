pkgname = "openimageio"
pkgver = "2.5.11.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    # disabled below
    "-DINSTALL_FONTS=OFF",
    "-DSTOP_ON_WARNING=OFF",
    "-DUSE_EXTERNAL_PUGIXML=ON",
    "-DUSE_QT=OFF",
]
make_check_args = [
    # missing testdata, tools, fonts
    # a few instances of output format diff
    # python tests try to self-import (which does not work)
    # non-x86-only (ppc64le, aarch64) failures:
    #   texture-crop, texture-interp-bilinear, texture-uint8, texture-skinny
    #   unit_compute (aarch64), unit_simd
    "-E",
    "(.*-broken|cmake-consumer|docs-examples-.*|filters|igrep|oiiotool|oiiotool-copy|oiiotool-subimage|oiiotool-text|python-.*|texture-crop|texture-interp-bilinear|texture-levels-stoch.*|texture-skinny|texture-udim.*|texture-uint8|unit_compute|unit_simd|unit_imageinout)",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "boost-devel",
    "ffmpeg-devel",
    "fmt-devel",
    "freetype-devel",
    "giflib-devel",
    "libheif-devel",
    "libpng-devel",
    "libraw-devel",
    "libtiff-devel",
    "libwebp-devel",
    "mesa-devel",
    "opencolorio-devel",
    "openexr-devel",
    "openjpeg-devel",
    "onetbb-devel",
    "pugixml-devel",
    "python-pybind11-devel",
    "robin-map",
]
checkdepends = ["bash", "fonts-dejavu"]
pkgdesc = "Toolset for manipulating VFX-related image file formats"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Apache-2.0"
url = "https://github.com/AcademySoftwareFoundation/OpenImageIO"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ebf1945e36679be55519d9f42a8f029c4a53d4efb4aaee3b10af6cdc93fb614b"
hardening = ["!int"]


@subpackage("openimageio-progs")
def _progs(self):
    return self.default_progs()


@subpackage("openimageio-devel")
def _devel(self):
    return self.default_devel()


@subpackage("python-openimageio")
def _python(self):
    self.pkgdesc = "Python bindings for openimageio"
    return ["usr/lib/python*"]
