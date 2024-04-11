pkgname = "openimageio"
pkgver = "2.5.10.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    # disabled below
    "-DBUILD_TESTING=OFF",
    "-DINSTALL_FONTS=OFF",
    "-DSTOP_ON_WARNING=OFF",
    "-DUSE_EXTERNAL_PUGIXML=ON",
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
    "qt6-qtbase-devel",
    "robin-map",
]
pkgdesc = "Toolset for manipulating VFX-related image file formats"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Apache-2.0"
url = "https://github.com/AcademySoftwareFoundation/OpenImageIO"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8f6a547f6a5d510737ba436f867043db537def65f0fdb14ec30e5a185b619f93"
# FIXME: tests are broken
options = ["!check"]

if self.profile().arch == "aarch64":
    # qopengl doesn't have desktop gl functions here
    configure_args += ["-DENABLE_iv=OFF"]


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
