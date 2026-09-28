pkgname = "xxhash"
pkgver = "0.8.4"
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
sha256 = "5738270935e7c3d38a79b3adf7c9692566ce7895a25f67de43ad52ab504acd32"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("xxhash-devel")
def _(self):
    return self.default_devel()
