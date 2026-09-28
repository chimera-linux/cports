pkgname = "libatasmart"
pkgver = "0.19"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--disable-static"]
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["udev-devel", "linux-headers"]
pkgdesc = "ATA S.M.A.R.T. reading and parsing library"
license = "LGPL-2.1-or-later"
url = "https://0pointer.de/blog/projects/being-smart.html"
source = f"https://0pointer.de/public/libatasmart-{pkgver}.tar.xz"
sha256 = "61f0ea345f63d28ab2ff0dc352c22271661b66bf09642db3a4049ac9dbdb0f8d"


@subpackage("libatasmart-devel")
def _(self):
    return self.default_devel()


@subpackage("libatasmart-progs")
def _(self):
    return self.default_progs()
