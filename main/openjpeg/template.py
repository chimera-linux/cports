pkgname = "openjpeg"
pkgver = "2.5.0"
pkgrel = 0
build_style = "cmake"
# we skip static libs or they get referenced in cmake devel files
configure_args = ["-DBUILD_TESTING=ON", "-DBUILD_STATIC_LIBS=OFF"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["libpng-devel", "libtiff-devel", "lcms2-devel"]
pkgdesc = "Open-source JPEG 2000 codec written in C"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://www.openjpeg.org"
source = f"https://github.com/uclouvain/openjpeg/archive/v{pkgver}.tar.gz"
sha256 = "0333806d6adecc6f7a91243b2b839ff4d2053823634d4f6ed7a59bc87409122a"
hardening = ["!cfi"]  # TODO
# missing test data
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("openjpeg-devel")
def _devel(self):
    # because cmake is dumb and references binaries in the find file
    self.depends += [f"openjpeg-progs={pkgver}-r{pkgrel}"]

    return self.default_devel(extra=["usr/lib/openjpeg-2.*"])


@subpackage("openjpeg-progs")
def _progs(self):
    return self.default_progs()
