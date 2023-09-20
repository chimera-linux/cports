pkgname = "libsecret"
pkgver = "0.21.1"
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
sha256 = "674f51323a5f74e4cb7e3277da68b5afddd333eca25bc9fd2d820a92972f90b1"
# does not work in container
options = ["!check", "!cross"]

tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}


@subpackage("libsecret-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libsecret-progs")
def _progs(self):
    return self.default_progs()
