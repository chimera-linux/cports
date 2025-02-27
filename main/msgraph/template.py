pkgname = "msgraph"
pkgver = "0.2.3"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dgtk_doc=false"]
hostmakedepends = ["gobject-introspection", "meson", "pkgconf"]
makedepends = [
    "glib-devel",
    "gnome-online-accounts-devel",
    "json-glib-devel",
    "libsoup-devel",
]
checkdepends = ["libxml2-devel", "uhttpmock-devel"]
pkgdesc = "GLib-based library for MS Graph protocol"
license = "LGPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/msgraph"
source = f"$(GNOME_SITE)/msgraph/{pkgver[:-2]}/msgraph-{pkgver}.tar.xz"
sha256 = "ed42e800cb7f0a07477cd9e3e744cdc1a240a6ad7ab96b8a875806267a9fddb0"
options = ["!cross"]


@subpackage("msgraph-devel")
def _(self):
    return self.default_devel()
