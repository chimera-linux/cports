pkgname = "openjpeg"
pkgver = "2.5.4"
pkgrel = 0
build_style = "cmake"
# we skip static libs or they get referenced in cmake devel files
configure_args = ["-DBUILD_TESTING=ON", "-DBUILD_STATIC_LIBS=OFF"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["libpng-devel", "libtiff-devel", "lcms2-devel"]
pkgdesc = "Open-source JPEG 2000 codec written in C"
license = "BSD-2-Clause"
url = "https://www.openjpeg.org"
source = f"https://github.com/uclouvain/openjpeg/archive/v{pkgver}.tar.gz"
sha256 = "a695fbe19c0165f295a8531b1e4e855cd94d0875d2f88ec4b61080677e27188a"
hardening = ["!vis", "!cfi"]
# missing test data
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("openjpeg-devel")
def _(self):
    # because cmake is dumb and references binaries in the find file
    self.depends += [self.with_pkgver("openjpeg-progs")]

    return self.default_devel()


@subpackage("openjpeg-progs")
def _(self):
    return self.default_progs()
