pkgname = "libatasmart"
pkgver = "0.19"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]
hostmakedepends = ["pkgconf"]
makedepends = ["udev-devel", "linux-headers"]
pkgdesc = "ATA S.M.A.R.T. reading and parsing library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://0pointer.de/blog/projects/being-smart.html"
source = f"https://0pointer.de/public/{pkgname}-{pkgver}.tar.xz"
sha256 = "61f0ea345f63d28ab2ff0dc352c22271661b66bf09642db3a4049ac9dbdb0f8d"

@subpackage("libatasmart-devel")
def _devel(self):
    return self.default_devel()

@subpackage("libatasmart-progs")
def _progs(self):
    return self.default_progs()

configure_gen = []
