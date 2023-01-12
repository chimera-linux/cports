pkgname = "exiv2"
pkgver = "0.27.5"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DEXIV2_BUILD_SAMPLES=OFF", "-DEXIV2_ENABLE_BMFF=ON",
    "-DEXIV2_BUILD_UNIT_TESTS=OFF"
]
make_check_target = "unit_test"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["libexpat-devel", "zlib-devel"]
pkgdesc = "Image metadata manipulation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.exiv2.org"
source = f"https://github.com/Exiv2/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}-Source.tar.gz"
sha256 = "35a58618ab236a901ca4928b0ad8b31007ebdc0386d904409d825024e45ea6e2"
# would need careful testing, maybe for when we enable check
hardening = ["!vis"]
# needs gtest
options = ["!check"]

@subpackage("exiv2-devel")
def _devel(self):
    return self.default_devel()
