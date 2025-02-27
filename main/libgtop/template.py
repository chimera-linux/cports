pkgname = "libgtop"
pkgver = "2.41.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-libgtop-smp", "--enable-introspection"]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gobject-introspection",
    "gtk-doc-tools",
    "libtool",
    "perl",
    "pkgconf",
]
makedepends = ["glib-devel", "libxau-devel", "linux-headers"]
pkgdesc = "GNOME library to retrieve system information"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/libgtop"
source = f"$(GNOME_SITE)/libgtop/{pkgver[:-2]}/libgtop-{pkgver}.tar.xz"
sha256 = "775676df958e2ea2452f7568f28b2ea581063d312773dd5c0b7624c1b9b2da8c"
file_modes = {
    "usr/libexec/libgtop_server2": ("root", "root", 0o4755),
}


@subpackage("libgtop-devel")
def _(self):
    return self.default_devel()
