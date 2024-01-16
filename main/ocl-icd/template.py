pkgname = "ocl-icd"
pkgver = "2.3.2"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = ["./bootstrap"]
make_cmd = "gmake"
hostmakedepends = [
    "gmake",
    "pkgconf",
    "ruby",
    "asciidoc",
    "automake",
    "libtool",
]
makedepends = ["opencl-headers"]
pkgdesc = "Generic OpenCL ICD loader"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://forge.imag.fr/projects/ocl-icd"
source = f"https://github.com/OCL-dev/ocl-icd/archive/v{pkgver}.tar.gz"
sha256 = "ec47d7dcd961ea06695b067e8b7edb82e420ddce03e0081a908c62fd0b8535c5"
# test suite weirdness
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("ocl-icd-devel")
def _devel(self):
    self.depends += ["opencl-headers"]

    return self.default_devel(extra=["usr/share/doc"])
