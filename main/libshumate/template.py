pkgname = "libshumate"
pkgver = "1.3_rc"
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
source = f"$(GNOME_SITE)/libshumate/{pkgver[:3]}/libshumate-{pkgver.replace('_', '.')}.tar.xz"
sha256 = "9b485d5d54de77b003dd19643f9614183279fa08de2520e2eb8a5eb10031390c"
options = ["!cross"]


@subpackage("libshumate-devel")
def _(self):
    return self.default_devel()
