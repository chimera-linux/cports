pkgname = "libucontext"
pkgver = "1.3.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "scdoc"]
pkgdesc = "Implementation of ucontext featuring glibc-compatible ABI"
maintainer = "eater <=@eater.me>"
license = "ISC"
url = "https://github.com/kaniini/libucontext"
source = f"{url}/archive/refs/tags/libucontext-{pkgver}.tar.gz"
sha256 = "1243ee9f03ad38e624f6844427b7bc1f0a05aa5de70f15f3b03805a364b971d6"
# see common-trampoline.c (1.3.1) libucontext_trampoline comment
options = ["!framepointer"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libucontext-devel")
def _(self):
    return self.default_devel()
