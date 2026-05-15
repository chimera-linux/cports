pkgname = "libshumate"
pkgver = "1.6.1"
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
source = f"$(GNOME_SITE)/libshumate/{'.'.join(pkgver.split('.')[0:2])}/libshumate-{pkgver}.tar.xz"
sha256 = "b36aad34500791785f546684d0f2ed644e4819ff4e85ae67a2245f159eccb2d4"
options = ["!cross"]


@subpackage("libshumate-devel")
def _(self):
    return self.default_devel()
