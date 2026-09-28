pkgname = "libatomic_ops"
pkgver = "7.8.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-static", "--enable-shared"]
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "Library for atomic operations"
license = "MIT AND GPL-2.0-or-later"
url = "https://github.com/ivmai/libatomic_ops"
source = f"{url}/releases/download/v{pkgver}/libatomic_ops-{pkgver}.tar.gz"
sha256 = "2356e002e80ef695875e971d6a4fd8c61ca5c6fa4fd1bf31cce54a269c8bfcd5"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libatomic_ops-devel")
def _(self):
    return self.default_devel()
