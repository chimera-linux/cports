pkgname = "openvdb"
pkgver = "11.0.0"
pkgrel = 3
build_style = "cmake"
configure_args = [
    "-DOPENVDB_CORE_STATIC=OFF",  # 1.4gb lol
    "-DOPENVDB_BUILD_NANOVDB=ON",
    "-DOPENVDB_BUILD_PYTHON_MODULE=ON",
    "-DOPENVDB_BUILD_UNITTESTS=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "c-blosc-devel",
    "gtest-devel",
    "onetbb-devel",
    "python-devel",
    "python-pybind11-devel",
]
pkgdesc = "Sparse volume data tools"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MPL-2.0"
url = "https://www.openvdb.org"
source = f"https://github.com/AcademySoftwareFoundation/openvdb/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6314ff1db057ea90050763e7b7d7ed86d8224fcd42a82cdbb9c515e001b96c74"
# 4 unittests fail outside of x86_64 with no easy way to skip them
options = []

if self.profile().arch != "x86_64":
    options += ["!check"]


@subpackage("openvdb-devel")
def _(self):
    return self.default_devel()


@subpackage("openvdb-progs")
def _(self):
    return self.default_progs()


@subpackage("python-pyopenvdb")
def _(self):
    self.subdesc = "python bindings"
    return ["usr/lib/python*"]
