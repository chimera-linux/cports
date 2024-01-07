pkgname = "ldacbt"
pkgver = "2.0.2.3"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "AOSP libldac dispatcher"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/EHfive/ldacBT"
source = f"{url}/releases/download/v{pkgver}/ldacBT-{pkgver}.tar.gz"
sha256 = "4bd8eece78bb5c1361fab95743e7100506e2408a25c4a592a0f8d349746dc5b4"
# no test suite
options = ["!check"]

if self.profile().endian == "big":
    broken = "big endian is not supported"


@subpackage("ldacbt-devel")
def _devel(self):
    return self.default_devel()
