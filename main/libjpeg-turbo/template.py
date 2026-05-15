pkgname = "libjpeg-turbo"
pkgver = "3.1.4.1"
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
sha256 = "ecae8008e2cc9ade2f2c1bb9d5e6d4fb73e7c433866a056bd82980741571a022"

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
