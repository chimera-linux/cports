pkgname = "opencolorio"
pkgver = "2.3.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    # disabled below
    "-DOCIO_BUILD_TESTS=OFF",
    "-DOPENGL_opengl_LIBRARY=/usr/lib/libGL.so",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "python",
]
makedepends = [
    "freeglut-devel",
    "glew-devel",
    "imath-devel",
    "lcms2-devel",
    "libexpat-devel",
    "minizip-ng-devel",
    "openexr-devel",
    "pystring-devel",
    "python-devel",
    "python-pybind11-devel",
    "yaml-cpp-devel",
    "zlib-devel",
]
pkgdesc = "Color management framework"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "BSD-3-Clause"
url = "https://opencolorio.org"
source = f"https://github.com/AcademySoftwareFoundation/OpenColorIO/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6bbf4e7fa4ea2f743a238cb22aff44890425771a2f57f62cece1574e46ceec2f"
# FIXME: ??
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("opencolorio-devel")
def _devel(self):
    return self.default_devel()


@subpackage("opencolorio-progs")
def _progs(self):
    return self.default_progs()


@subpackage("python-opencolorio")
def _python(self):
    self.pkgdesc = "Python bindings for opencolorio"
    return ["usr/lib/python*"]
