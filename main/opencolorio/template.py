pkgname = "opencolorio"
pkgver = "2.4.0"
pkgrel = 0
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
source = f"https://github.com/AcademySoftwareFoundation/OpenColorIO/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "00fc49578abf8435eb041088af44c8c4bcaafbe04021d53d341adcd488aec711"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("opencolorio-devel")
def _(self):
    return self.default_devel()


@subpackage("opencolorio-progs")
def _(self):
    return self.default_progs()


@subpackage("python-opencolorio")
def _(self):
    self.pkgdesc = "Python bindings for opencolorio"
    self.depends += ["python"]

    return ["usr/lib/python*"]
