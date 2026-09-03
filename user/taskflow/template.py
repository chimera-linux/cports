pkgname = "taskflow"
pkgver = "4.1.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DTF_BUILD_EXAMPLES=OFF"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "General-purpose task-parallel programming system in C++"
license = "MIT"
url = "https://github.com/taskflow/taskflow"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2107f90e315e48a676922010b036357ff2b0c6b9160ce17fa9396e5860b1d715"
# signed overflow in unittests (scan/sort/dependent_asyncs)
hardening = ["!int"]

if self.profile().cross:
    # doctest execs tests during build, not check, so cbuild's cross skip doesn't help
    configure_args += ["-DTF_BUILD_TESTS=OFF"]


def post_install(self):
    self.install_license("LICENSE")
