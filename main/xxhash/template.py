pkgname = "xxhash"
pkgver = "0.8.3"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
# sporadically breaks in parallel
make_check_args = ["-j1"]
make_use_env = True
hostmakedepends = ["pkgconf"]
pkgdesc = "Fast non-cryptographic hashing algorithm"
license = "BSD-2-Clause"
url = "https://cyan4973.github.io/xxHash"
source = f"https://github.com/Cyan4973/xxhash/archive/v{pkgver}.tar.gz"
sha256 = "aae608dfe8213dfd05d909a57718ef82f30722c392344583d3f39050c7f29a80"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("xxhash-devel")
def _(self):
    return self.default_devel()
