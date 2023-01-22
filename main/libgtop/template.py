pkgname = "libgtop"
pkgver = "2.40.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-libgtop-smp", "--enable-introspection"]
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf", "perl", "gobject-introspection"]
makedepends = ["libglib-devel", "libxau-devel", "linux-headers"]
pkgdesc = "GNOME library to retrieve system information"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/libgtop"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "78f3274c0c79c434c03655c1b35edf7b95ec0421430897fb1345a98a265ed2d4"
# glib
hardening = ["!vis"]

@subpackage("libgtop-devel")
def _devel(self):
    return self.default_devel()
