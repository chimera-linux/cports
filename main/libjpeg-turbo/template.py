pkgname = "libjpeg-turbo"
pkgver = "3.1.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DWITH_JPEG8=1",
    "-DCMAKE_INSTALL_LIBDIR=/usr/lib",
    "-DENABLE_STATIC=FALSE",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "nasm"]
pkgdesc = "Derivative of libjpeg which uses SIMD instructions"
license = "IJG AND BSD-3-Clause AND Zlib"
url = "https://libjpeg-turbo.org"
source = f"https://github.com/libjpeg-turbo/libjpeg-turbo/releases/download/{pkgver}/libjpeg-turbo-{pkgver}.tar.gz"
sha256 = "aadc97ea91f6ef078b0ae3a62bba69e008d9a7db19b34e4ac973b19b71b4217c"

# tests segfault with altivec simd
# also some floattest12 tests fail
match self.profile().arch:
    case "ppc64le" | "ppc64" | "ppc":
        configure_args += ["-DWITH_SIMD=FALSE", "-DFLOATTEST12="]
    case "aarch64":
        configure_args += ["-DFLOATTEST12="]


def post_install(self):
    self.install_license("LICENSE.md")

    self.install_file("src/jpegint.h", "usr/include")
    self.install_file("src/transupp.h", "usr/include")

    self.uninstall("usr/share/doc")
    self.uninstall("usr/bin/tjbench")


@subpackage("libjpeg-turbo-devel")
def _(self):
    return self.default_devel()


@subpackage("libjpeg-turbo-progs")
def _(self):
    return self.default_progs()
