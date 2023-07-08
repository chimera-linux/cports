pkgname = "libjpeg-turbo"
pkgver = "3.0.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DWITH_JPEG8=1", "-DCMAKE_INSTALL_LIBDIR=/usr/lib"]
hostmakedepends = ["cmake", "ninja", "pkgconf", "nasm"]
pkgdesc = "Derivative of libjpeg which uses SIMD instructions"
maintainer = "q66 <q66@chimera-linux.org>"
license = "IJG AND BSD-3-Clause AND Zlib"
url = "https://libjpeg-turbo.org"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "c77c65fcce3d33417b2e90432e7a0eb05f59a7fff884022a9d931775d583bfaa"

# tests segfault with altivec simd
# also some floattest12 tests fail
match self.profile().arch:
    case "ppc64le" | "ppc64" | "ppc":
        configure_args += ["-DWITH_SIMD=FALSE", "-DFLOATTEST12="]


def post_install(self):
    self.install_license("LICENSE.md")

    self.install_file("jpegint.h", "usr/include")
    self.install_file("transupp.h", "usr/include")

    self.rm(self.destdir / "usr/share/doc", recursive=True)
    self.rm(self.destdir / "usr/bin/tjbench")


@subpackage("libjpeg-turbo-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libjpeg-turbo-progs")
def _progs(self):
    return self.default_progs()
