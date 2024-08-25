pkgname = "usrsctp"
pkgver = "0.9.5.0"
pkgrel = 2
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Portable SCTP userland stack"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/sctplab/usrsctp"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "260107caf318650a57a8caa593550e39bca6943e93f970c80d6c17e59d62cd92"
# vis breaks symbols
hardening = ["!vis"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("usrsctp-devel")
def _(self):
    return self.default_devel()
