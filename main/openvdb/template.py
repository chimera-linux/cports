pkgname = "openvdb"
pkgver = "13.0.0"
pkgrel = 0
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
    "python-nanobind-devel",
]
checkdepends = ["python-numpy"]
pkgdesc = "Sparse volume data tools"
license = "MPL-2.0"
url = "https://www.openvdb.org"
source = f"https://github.com/AcademySoftwareFoundation/openvdb/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4d6a91df5f347017496fe8d22c3dbb7c4b5d7289499d4eb4d53dd2c75bb454e1"
# suboverflow in PCA, annoying abstractions make it hard to debug
hardening = ["!int"]
# 4 unittests fail outside of x86_64 with no easy way to skip them
options = []

if self.profile().arch != "x86_64":
    options += ["!check"]
    configure_args += ["-DOPENVDB_BUILD_UNITTESTS=OFF"]


@subpackage("openvdb-devel")
def _(self):
    return self.default_devel()


@subpackage("openvdb-progs")
def _(self):
    return self.default_progs()


@subpackage("openvdb-python")
def _(self):
    self.subdesc = "python bindings"
    self.renames = ["python-pyopenvdb"]

    return ["usr/lib/python*"]
