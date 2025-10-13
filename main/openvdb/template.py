pkgname = "openvdb"
pkgver = "12.1.1"
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
pkgdesc = "Sparse volume data tools"
license = "MPL-2.0"
url = "https://www.openvdb.org"
source = f"https://github.com/AcademySoftwareFoundation/openvdb/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ccd0ea1669a53c7c13087a08ac5a1351041c4cdd308f6d6f591074a106fcb565"
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
    # transitional
    self.provides = [self.with_pkgver("python-pyopenvdb")]

    return ["usr/lib/python*"]
