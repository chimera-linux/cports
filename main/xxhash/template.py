pkgname = "xxhash"
pkgver = "0.8.1"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_check_target = "test"
make_use_env = True
hostmakedepends = ["gmake", "pkgconf"]
pkgdesc = "Fast non-cryptographic hashing algorithm"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://cyan4973.github.io/xxHash"
source = f"https://github.com/Cyan4973/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "3bb6b7d6f30c591dd65aaaff1c8b7a5b94d81687998ca9400082c739a690436c"

def post_install(self):
    self.install_license("LICENSE")

@subpackage("xxhash-devel")
def _devel(self):
    return self.default_devel()
