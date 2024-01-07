pkgname = "libucontext"
pkgver = "1.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "ninja", "pkgconf", "scdoc"]
pkgdesc = "Implementation of ucontext featuring glibc-compatible ABI"
maintainer = "eater <=@eater.me>"
license = "ISC"
url = "https://github.com/kaniini/libucontext"
source = (
    f"https://github.com/kaniini/libucontext/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "2657e087c493263e7bbbde152a5bc08ce22dc5a7970887ac4fd251b90b58401f"


@subpackage("libucontext-devel")
def _devel(self):
    return self.default_devel()
