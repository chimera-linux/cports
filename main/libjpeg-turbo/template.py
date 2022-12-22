pkgname = "libjpeg-turbo"
pkgver = "2.1.4"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DWITH_JPEG8=1", "-DCMAKE_INSTALL_LIBDIR=/usr/lib"]
hostmakedepends = ["cmake", "ninja", "pkgconf", "yasm"]
pkgdesc = "Derivative of libjpeg which uses SIMD instructions"
maintainer = "q66 <q66@chimera-linux.org>"
license = "IJG AND BSD-3-Clause AND Zlib"
url = "https://libjpeg-turbo.org"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "d3ed26a1131a13686dfca4935e520eb7c90ae76fbc45d98bb50a8dc86230342b"

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

# FIXME visibility
hardening = ["!vis"]
