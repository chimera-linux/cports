pkgname = "libjpeg-turbo"
pkgver = "3.0.3"
pkgrel = 2
build_style = "cmake"
configure_args = [
    "-DWITH_JPEG8=1",
    "-DCMAKE_INSTALL_LIBDIR=/usr/lib",
    "-DENABLE_STATIC=FALSE",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "nasm"]
pkgdesc = "Derivative of libjpeg which uses SIMD instructions"
maintainer = "q66 <q66@chimera-linux.org>"
license = "IJG AND BSD-3-Clause AND Zlib"
url = "https://libjpeg-turbo.org"
source = f"https://github.com/libjpeg-turbo/libjpeg-turbo/releases/download/{pkgver}/libjpeg-turbo-{pkgver}.tar.gz"
sha256 = "343e789069fc7afbcdfe44dbba7dbbf45afa98a15150e079a38e60e44578865d"

# tests segfault with altivec simd
# also some floattest12 tests fail
match self.profile().arch:
    case "ppc64le" | "ppc64" | "ppc":
        configure_args += ["-DWITH_SIMD=FALSE", "-DFLOATTEST12="]
    case "aarch64":
        configure_args += ["-DFLOATTEST12="]


def post_install(self):
    self.install_license("LICENSE.md")

    self.install_file("jpegint.h", "usr/include")
    self.install_file("transupp.h", "usr/include")

    self.uninstall("usr/share/doc")
    self.uninstall("usr/bin/tjbench")


@subpackage("libjpeg-turbo-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libjpeg-turbo-progs")
def _progs(self):
    return self.default_progs()
