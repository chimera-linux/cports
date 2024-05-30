pkgname = "libshumate"
pkgver = "1.2.2"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dgtk_doc=false"]
make_check_env = {"GTK_A11Y": "none"}
make_check_wrapper = ["wlheadless-run", "--"]
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
checkdepends = ["xwayland-run"]
pkgdesc = "GTK library to display maps"
maintainer = "triallax <triallax@tutanota.com>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libshumate"
source = f"$(GNOME_SITE)/libshumate/{pkgver[:-2]}/libshumate-{pkgver}.tar.xz"
sha256 = "6f587579f7f2d60b38d3f4727eb1a8d2feac9cbdc018e53ff5f772a8608fa44b"
options = ["!cross"]


@subpackage("libshumate-devel")
def _devel(self):
    return self.default_devel()
