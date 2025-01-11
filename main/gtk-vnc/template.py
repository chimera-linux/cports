pkgname = "gtk-vnc"
pkgver = "1.4.0"
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
    "zlib-ng-compat-devel",
]
pkgdesc = "VNC client viewer widget for GTK+3"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/gtk-vnc"
source = f"$(GNOME_SITE)/gtk-vnc/{pkgver[:-2]}/gtk-vnc-{pkgver}.tar.xz"
sha256 = "1be64c4e4760c52b3ec33067290d1efa40ad4cecab6c673813804e3c559d9683"


@subpackage("gtk-vnc-devel")
def _(self):
    return self.default_devel()
