pkgname = "gtk-vnc"
pkgver = "1.5.0"
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
    "gobject-introspection-devel",
    "gtk+3-devel",
    "libgcrypt-devel",
    "libpulse-devel",
    "libsasl-devel",
    "vala-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "VNC client viewer widget for GTK+3"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/gtk-vnc"
source = f"$(GNOME_SITE)/gtk-vnc/{pkgver[:-2]}/gtk-vnc-{pkgver}.tar.xz"
sha256 = "c0beb4747528ad931da43acc567c6a0190f7fc624465571ed9ccece02c34dd23"


@subpackage("gtk-vnc-devel")
def _(self):
    return self.default_devel()
