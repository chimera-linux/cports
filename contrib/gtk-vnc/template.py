pkgname = "gtk-vnc"
pkgver = "1.3.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dintrospection=enabled",
    "-Dpulseaudio=enabled",
    "-Dsasl=enabled",
    "-Dwith-vala=enabled",
    "-Dwith-coroutine=gthread",
]
hostmakedepends = [
    "gettext",
    "gobject-introspection",
    "meson",
    "perl",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "gdk-pixbuf-devel",
    "gnutls-devel",
    "gtk+3-devel",
    "libgcrypt-devel",
    "libgirepository-devel",
    "libpulse-devel",
    "libsasl-devel",
    "vala-devel",
    "zlib-devel",
]
pkgdesc = "VNC client viewer widget for GTK+3"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/gtk-vnc"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "512763ac4e0559d0158b6682ca5dd1a3bd633f082f5e4349d7158e6b5f80f1ce"


@subpackage("gtk-vnc-devel")
def _devel(self):
    return self.default_devel()
