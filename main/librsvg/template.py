pkgname = "librsvg"
pkgver = "2.56.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-introspection", "--enable-vala", "--disable-static",
    "--disable-gtk-doc",
]
make_cmd = "gmake"
hostmakedepends = [
    "gmake", "pkgconf", "cargo", "python", "gobject-introspection",
    "glib-devel", "gdk-pixbuf-devel", "vala", "python-docutils",
]
makedepends = [
    "rust", "vala-devel", "cairo-devel", "pango-devel", "freetype-devel",
    "gdk-pixbuf-devel", "glib-devel", "libxml2-devel",
]
provides = [f"gdk-pixbuf-loader-svg={pkgver}-r{pkgrel}"]
pkgdesc = "SVG library for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/LibRsvg"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "194b5097d9cd107495f49c291cf0da65ec2b4bb55e5628369751a3f44ba222b3"
# sample files may differ based on pango/freetype/harfbuzz version
options = ["!check", "!cross"]

def do_prepare(self):
    from cbuild.util import cargo
    cargo.Cargo(self).vendor(wrksrc = ".")
    cargo.setup_vendor(self)

def post_patch(self):
    from cbuild.util import cargo
    cargo.clear_vendor_checksums(self, "system-deps")

@subpackage("librsvg-devel")
def _devel(self):
    return self.default_devel()

@subpackage("librsvg-progs")
def _progs(self):
    return self.default_progs()
