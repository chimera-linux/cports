pkgname = "libshumate"
pkgver = "1.2.1"
pkgrel = 1
build_style = "meson"
configure_args = ["-Dgtk_doc=false"]
make_check_env = {"GTK_A11Y": "none"}
make_check_wrapper = ["weston-headless-run"]
hostmakedepends = [
    "gobject-introspection",
    "gperf",
    "meson",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "glib-devel",
    "gtk4-devel",
    "json-glib-devel",
    "libsoup-devel",
    "protobuf-c-devel",
    "sqlite-devel",
]
checkdepends = ["weston"]
pkgdesc = "GTK library to display maps"
maintainer = "triallax <triallax@tutanota.com>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libshumate"
source = f"$(GNOME_SITE)/libshumate/{pkgver[:-2]}/libshumate-{pkgver}.tar.xz"
sha256 = "1105ee077e2147f2a039cddfa616fa5cb9438883dd940427e11699dcd6549c11"
options = ["!cross"]


@subpackage("libshumate-devel")
def _devel(self):
    return self.default_devel()
