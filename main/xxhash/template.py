pkgname = "xxhash"
pkgver = "0.8.2"
pkgrel = 1
build_style = "makefile"
make_cmd = "gmake"
make_check_target = "test"
# sporadically breaks in parallel
make_check_args = ["-j1"]
make_use_env = True
hostmakedepends = ["gmake", "pkgconf"]
pkgdesc = "Fast non-cryptographic hashing algorithm"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://cyan4973.github.io/xxHash"
source = f"https://github.com/Cyan4973/xxhash/archive/v{pkgver}.tar.gz"
sha256 = "baee0c6afd4f03165de7a4e67988d16f0f2b257b51d0e3cb91909302a26a79c4"


if self.profile().arch == "x86_64":
    # on x86_64, there can be runtime dispatch for sse/avx etc
    # this is not automatically detected by the makefile
    make_build_args = ["DISPATCH=1"]
    # XXX: rebuilds in install so pass twice
    make_install_args = ["DISPATCH=1"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("xxhash-devel")
def _devel(self):
    return self.default_devel()
