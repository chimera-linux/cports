pkgname = "ocl-icd"
pkgver = "2.3.5"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = ["./bootstrap"]
hostmakedepends = [
    "asciidoc",
    "automake",
    "libtool",
    "pkgconf",
    "ruby",
]
makedepends = ["opencl-headers"]
pkgdesc = "Generic OpenCL ICD loader"
license = "BSD-2-Clause"
url = "https://forge.imag.fr/projects/ocl-icd"
source = f"https://github.com/OCL-dev/ocl-icd/archive/v{pkgver}.tar.gz"
sha256 = "cdd7984425fa92d37273eee4180b5f57b047eda6dd8fd623e58498f844b09b75"
# test suite weirdness
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("ocl-icd-devel")
def _(self):
    self.depends += ["opencl-headers"]

    return self.default_devel(extra=["usr/share/doc"])
