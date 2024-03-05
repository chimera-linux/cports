pkgname = "libsecret"
pkgver = "0.21.4"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dgtk_doc=false"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "xsltproc",
    "docbook-xsl-nons",
    "gobject-introspection",
    "vala",
]
makedepends = ["glib-devel", "libgcrypt-devel", "vala"]
pkgdesc = "GObject-based library for accessing the Secret Service API"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libsecret"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "163d08d783be6d4ab9a979ceb5a4fecbc1d9660d3c34168c581301cd53912b20"
# does not work in container
options = ["!check", "!cross"]


@subpackage("libsecret-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libsecret-progs")
def _progs(self):
    return self.default_progs()
