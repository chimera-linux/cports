pkgname = "libgtop"
pkgver = "2.41.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-libgtop-smp", "--enable-introspection"]
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf", "perl", "gobject-introspection"]
makedepends = ["glib-devel", "libxau-devel", "linux-headers"]
pkgdesc = "GNOME library to retrieve system information"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/libgtop"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "43ea9ad13f7caf98303e64172b191be9b96bab340b019deeec72251ee140fe3b"
suid_files = [
    "usr/libexec/libgtop_server2",
]


@subpackage("libgtop-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
