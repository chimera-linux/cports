pkgname = "lensfun"
pkgver = "0.3.4"
pkgrel = 3
build_style = "cmake"
configure_args = [
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
    "-DINSTALL_HELPER_SCRIPTS=OFF",
    "-DBUILD_TESTS=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "python-setuptools"]
makedepends = ["glib-devel"]
pkgdesc = "Photographic lens distortion library"
license = "LGPL-3.0-only AND CC-BY-SA-3.0"
url = "https://lensfun.github.io"
source = (
    f"https://github.com/lensfun/lensfun/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "dafb39c08ef24a0e2abd00d05d7341b1bf1f0c38bfcd5a4c69cf5f0ecb6db112"

if self.profile().arch in [
    "aarch64",
    "loongarch64",
    "ppc64le",
    "ppc64",
    "riscv64",
    "x86_64",
]:
    makedepends += ["libomp-devel"]
else:
    configure_args += ["-DBUILD_TESTS=OFF"]


@subpackage("lensfun-devel")
def _(self):
    return self.default_devel()
