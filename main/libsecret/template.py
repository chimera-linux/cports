pkgname = "libsecret"
pkgver = "0.21.6"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dgtk_doc=false"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "libxslt-progs",
    "docbook-xsl-nons",
    "gobject-introspection",
    "vala",
]
makedepends = ["glib-devel", "libgcrypt-devel", "vala"]
pkgdesc = "GObject-based library for accessing the Secret Service API"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libsecret"
source = f"$(GNOME_SITE)/libsecret/{pkgver[:-2]}/libsecret-{pkgver}.tar.xz"
sha256 = "747b8c175be108c880d3adfb9c3537ea66e520e4ad2dccf5dce58003aeeca090"
# does not work in container
options = ["!check", "!cross"]


@subpackage("libsecret-devel")
def _(self):
    return self.default_devel()


@subpackage("libsecret-progs")
def _(self):
    return self.default_progs()
