pkgname = "libsecret"
pkgver = "0.20.4"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gtk-doc-tools", "xsltproc",
    "gobject-introspection", "vala"
]
makedepends = ["libglib-devel", "libgcrypt-devel", "vala"]
pkgdesc = "GObject-based library for accessing the Secret Service API"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libsecret"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "325a4c54db320c406711bf2b55e5cb5b6c29823426aa82596a907595abb39d28"
# does not work in container
options = ["!check"]

@subpackage("libsecret-devel")
def _devel(self):
    return self.default_devel(extra = ["usr/share/gtk-doc"])

@subpackage("libsecret-progs")
def _progs(self):
    return self.default_progs()
