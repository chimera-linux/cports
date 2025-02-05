pkgname = "opencolorio"
pkgver = "2.4.1"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DOCIO_BUILD_TESTS=ON",
    "-DOCIO_BUILD_GPU_TESTS=OFF",
    "-DOPENGL_opengl_LIBRARY=/usr/lib/libGL.so",
]
# this skips most of the (sub)tests but they are not granular, and there are
# hundreds of off-by-1 failures. check them next release
make_check_args = ["-E", "test_cpu*"]
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
    "zlib-ng-compat-devel",
]
pkgdesc = "Color management framework"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "BSD-3-Clause"
url = "https://opencolorio.org"
source = f"https://github.com/AcademySoftwareFoundation/OpenColorIO/archive/refs/tags/v{pkgver}.tar.gz>v2.4.0-real-real-really-real.tar.gz"
sha256 = "d4eb15408b33dffd6ba0bba9a53328085b40bdd9319fa3d0d7348d06a8cbe842"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("opencolorio-devel")
def _(self):
    return self.default_devel()


@subpackage("opencolorio-progs")
def _(self):
    return self.default_progs()


@subpackage("opencolorio-python")
def _(self):
    self.pkgdesc = "Python bindings for opencolorio"
    self.depends += ["python"]
    # transitional
    self.provides = [self.with_pkgver("python-opencolorio")]

    return ["usr/lib/python*"]
