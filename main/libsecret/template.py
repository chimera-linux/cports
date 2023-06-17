pkgname = "libsecret"
pkgver = "0.20.5"
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
sha256 = "3fb3ce340fcd7db54d87c893e69bfc2b1f6e4d4b279065ffe66dac9f0fd12b4d"
# does not work in container
options = ["!check", "!cross"]

tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}


@subpackage("libsecret-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libsecret-progs")
def _progs(self):
    return self.default_progs()
