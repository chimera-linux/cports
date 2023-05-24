pkgname = "ocl-icd"
pkgver = "2.3.1"
pkgrel = 0
build_style = "gnu_configure"
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
source = f"https://github.com/OCL-dev/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "a32b67c2d52ffbaf490be9fc18b46428ab807ab11eff7664d7ff75e06cfafd6d"
# test suite weirdness
options = ["!check"]


def pre_configure(self):
    self.do(self.chroot_cwd / "bootstrap")


def post_install(self):
    self.install_license("COPYING")


@subpackage("ocl-icd-devel")
def _devel(self):
    self.depends += ["opencl-headers"]

    return self.default_devel(extra=["usr/share/doc"])


configure_gen = []
