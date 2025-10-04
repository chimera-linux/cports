pkgname = "openimageio"
pkgver = "3.0.10.0"
pkgrel = 1
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
    #   texture-texture3d, unit_compute (aarch64), unit_simd, maketx
    "-E",
    "(.*-broken|cmake-consumer|docs-examples-.*|filters|igrep|maketx|oiiotool|oiiotool-copy|oiiotool-subimage|oiiotool-text|python-.*|texture-crop|texture-interp-bilinear|texture-levels-stoch.*|texture-skinny|texture-texture3d|texture-udim.*|texture-uint8|unit_compute|unit_simd|unit_imageinout)",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "boost-devel",
    "ffmpeg-devel",
    "fmt-devel",
    "freetype-devel",
    "giflib-devel",
    "libheif-devel",
    "libjxl-devel",
    "libpng-devel",
    "libraw-devel",
    "libtiff-devel",
    "libwebp-devel",
    "mesa-devel",
    "onetbb-devel",
    "opencolorio-devel",
    "opencv-devel",
    "openexr-devel",
    "openjpeg-devel",
    "openvdb-devel",
    "ptex-devel",
    "pugixml-devel",
    "python-pybind11-devel",
    "robin-map",
]
checkdepends = ["bash", "fonts-dejavu"]
pkgdesc = "Toolset for manipulating VFX-related image file formats"
license = "Apache-2.0"
url = "https://github.com/AcademySoftwareFoundation/OpenImageIO"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c424637af66fc6d04f202156c3f7cf4a5484ccbe07966d3d8a1fde27c7472721"
# simulate release with none
tool_flags = {"CXXFLAGS": ["-DNDEBUG"]}
hardening = ["!int"]


@subpackage("openimageio-progs")
def _(self):
    return self.default_progs()


@subpackage("openimageio-devel")
def _(self):
    # referenced by cmake
    self.depends = ["opencv-devel"]

    return self.default_devel()


@subpackage("openimageio-python")
def _(self):
    self.pkgdesc = "Python bindings for openimageio"
    self.depends += ["python"]
    self.renames = ["python-openimageio"]

    return ["usr/lib/python*"]
