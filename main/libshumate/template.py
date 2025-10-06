pkgname = "libshumate"
pkgver = "1.5.0.1"
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
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libshumate"
source = f"$(GNOME_SITE)/libshumate/{pkgver[:-4]}/libshumate-{pkgver}.tar.xz"
sha256 = "a96fe7a9637ce819da121e83e26eb533cdc78c146fa51a960bbdcad557409e58"
options = ["!cross"]


@subpackage("libshumate-devel")
def _(self):
    return self.default_devel()
