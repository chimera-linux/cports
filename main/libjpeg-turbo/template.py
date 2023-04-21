pkgname = "libjpeg-turbo"
pkgver = "2.1.5.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DWITH_JPEG8=1", "-DCMAKE_INSTALL_LIBDIR=/usr/lib"]
hostmakedepends = ["cmake", "ninja", "pkgconf", "nasm"]
pkgdesc = "Derivative of libjpeg which uses SIMD instructions"
maintainer = "q66 <q66@chimera-linux.org>"
license = "IJG AND BSD-3-Clause AND Zlib"
url = "https://libjpeg-turbo.org"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "2fdc3feb6e9deb17adec9bafa3321419aa19f8f4e5dea7bf8486844ca22207bf"

# tests segfault with altivec simd
match self.profile().arch:
    case "ppc64le" | "ppc64":
        configure_args += ["-DWITH_SIMD=FALSE"]

def post_install(self):
    self.install_license("LICENSE.md")

    self.install_file("jpegint.h", "usr/include")
    self.install_file("transupp.h", "usr/include")

    self.rm(self.destdir / "usr/share/doc", recursive = True)
    self.rm(self.destdir / "usr/bin/tjbench")

@subpackage("libjpeg-turbo-devel")
def _devel(self):
    return self.default_devel()

@subpackage("libjpeg-turbo-progs")
def _progs(self):
    return self.default_progs()
