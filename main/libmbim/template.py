pkgname = "libmbim"
pkgver = "1.26.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static", "--enable-introspection"]
make_cmd = "gmake"
hostmakedepends = [
    "gmake", "pkgconf", "glib-devel", "libgudev-devel", "gobject-introspection"
]
makedepends = ["libglib-devel", "libgudev-devel", "linux-headers"]
pkgdesc = "MBIM modem protocol helper library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://www.freedesktop.org/wiki/Software/libmbim"
source = f"$(FREEDESKTOP_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "10c77bf5b5eb8c92ba80e9b519923ad9b898362bc8e1928e2bc9a17eeba649af"

@subpackage("libmbim-devel")
def _devel(self):
    return self.default_devel()
