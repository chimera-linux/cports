pkgname = "libucontext"
pkgver = "1.3.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "scdoc"]
pkgdesc = "Implementation of ucontext featuring glibc-compatible ABI"
maintainer = "eater <=@eater.me>"
license = "ISC"
url = "https://github.com/kaniini/libucontext"
source = f"{url}/archive/refs/tags/libucontext-{pkgver}.tar.gz"
sha256 = "4faf1838a15d61efe27ddac24fded2c290929eb3a1fefc72f952ae96d5bda006"
# see common-trampoline.c (1.3.1) libucontext_trampoline comment
options = ["!framepointer"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libucontext-devel")
def _(self):
    return self.default_devel()
