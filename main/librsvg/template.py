pkgname = "librsvg"
pkgver = "2.56.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-introspection",
    "--enable-vala",
    "--disable-static",
    "--disable-gtk-doc",
]
configure_gen = []
make_cmd = "gmake"
hostmakedepends = [
    "gmake",
    "pkgconf",
    "cargo",
    "python",
    "gobject-introspection",
    "glib-devel",
    "gdk-pixbuf-devel",
    "vala",
    "python-docutils",
]
makedepends = [
    "rust",
    "vala-devel",
    "cairo-devel",
    "pango-devel",
    "freetype-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "libxml2-devel",
]
provides = [f"gdk-pixbuf-loader-svg={pkgver}-r{pkgrel}"]
pkgdesc = "SVG library for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/LibRsvg"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "3ec3c4d8f73e0ba4b9130026969e8371c092b734298d36e2fdb3eb4afcec1200"
# sample files may differ based on pango/freetype/harfbuzz version
options = ["!check", "!cross"]


def do_prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor(wrksrc=".")
    cargo.setup_vendor(self)


def post_patch(self):
    from cbuild.util import cargo

    cargo.clear_vendor_checksums(self, "system-deps")
    cargo.clear_vendor_checksums(self, "rustix")


@subpackage("librsvg-devel")
def _devel(self):
    return self.default_devel()


@subpackage("librsvg-progs")
def _progs(self):
    return self.default_progs()
