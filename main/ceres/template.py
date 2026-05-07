pkgname = "ceres"
pkgver = "2.2.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "abseil-cpp-devel",
    "eigen",
    "gflags-devel",
    "glog-devel",
    "openblas-devel",
]
pkgdesc = "Non-linear optimization library"
license = "BSD-3-Clause AND Apache-2.0 AND MIT"
url = "http://ceres-solver.org"
source = f"https://github.com/ceres-solver/ceres-solver/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "12efacfadbfdc1bbfa203c236e96f4d3c210bed96994288b3ff0c8e7c6f350d4"
tool_flags = {"CXXFLAGS": []}
# fails some tests
hardening = ["!int"]

match self.profile().arch:
    case "ppc64" | "ppc":
        # vsx assumptions in altivec code
        tool_flags["CXXFLAGS"] += ["-DEIGEN_DONT_VECTORIZE"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("ceres-devel")
def _(self):
    self.depends += makedepends

    return self.default_devel()
