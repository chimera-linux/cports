pkgname = "libmbim"
pkgver = "1.26.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static", "--enable-introspection"]
make_cmd = "gmake"
hostmakedepends = [
    "gmake", "pkgconf", "glib-devel", "libgudev-devel", "gobject-introspection"
]
makedepends = ["glib-devel", "libgudev-devel", "linux-headers"]
pkgdesc = "MBIM modem protocol helper library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://www.freedesktop.org/wiki/Software/libmbim"
source = f"$(FREEDESKTOP_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "f688cec4c4586a17575f5e327448ce62f2000ef6a07c9e4589873d4a68568ad9"

@subpackage("libmbim-devel")
def _devel(self):
    return self.default_devel()
