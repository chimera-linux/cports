pkgname = "libgtop"
pkgver = "2.41.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-libgtop-smp", "--enable-introspection"]
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gmake",
    "gobject-introspection",
    "gtk-doc-tools",
    "libtool",
    "perl",
    "pkgconf",
]
makedepends = ["glib-devel", "libxau-devel", "linux-headers"]
pkgdesc = "GNOME library to retrieve system information"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/libgtop"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "d9026cd8a48d27cdffd332f8d60a92764b56424e522c420cd13a01f40daf92c3"
suid_files = [
    "usr/libexec/libgtop_server2",
]


@subpackage("libgtop-devel")
def _devel(self):
    return self.default_devel()
