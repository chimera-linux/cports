pkgname = "libsecret"
pkgver = "0.21.7"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dgtk_doc=false"]
hostmakedepends = [
    "docbook-xsl-nons",
    "glib-devel",
    "gobject-introspection",
    "libxslt-progs",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = ["glib-devel", "libgcrypt-devel", "vala"]
pkgdesc = "GObject-based library for accessing the Secret Service API"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libsecret"
source = f"$(GNOME_SITE)/libsecret/{pkgver[:-2]}/libsecret-{pkgver}.tar.xz"
sha256 = "6b452e4750590a2b5617adc40026f28d2f4903de15f1250e1d1c40bfd68ed55e"
# does not work in container
options = ["!check", "!cross"]


@subpackage("libsecret-devel")
def _(self):
    return self.default_devel()


@subpackage("libsecret-progs")
def _(self):
    return self.default_progs()
