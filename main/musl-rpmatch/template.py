pkgname = "musl-rpmatch"
pkgver = "1.0"
pkgrel = 0
build_style = "makefile"
make_build_args = ["PREFIX=/usr"]
hostmakedepends = ["pkgconf"]
pkgdesc = "Implementation of rpmatch(3) for musl libc"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/chimera-linux/musl-rpmatch"
source = f"{url}/archive/refs/tags/v{pkgver}-mk2.tar.gz"
sha256 = "a7b9649b49a8a59da09cf61228dc812cae6f0aea8be036788a9173c6f15a1a77"
# no test suite; also no point in LTOing this
options = ["bootstrap", "!check", "!lto"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("musl-rpmatch-devel")
def _devel(self):
    self.options = ["!splitstatic"]
    return self.default_devel()
