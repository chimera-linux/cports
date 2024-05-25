pkgname = "librsvg"
pkgver = "2.58.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-introspection",
    "--enable-vala",
    "--disable-static",
    "--disable-gtk-doc",
]
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "cargo",
    "gdk-pixbuf-devel",
    "glib-devel",
    "gmake",
    "gobject-introspection",
    "libtool",
    "pkgconf",
    "python",
    "python-docutils",
    "vala",
]
makedepends = [
    "cairo-devel",
    "freetype-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "libxml2-devel",
    "pango-devel",
    "rust-std",
    "vala-devel",
]
provides = [f"gdk-pixbuf-loader-svg={pkgver}-r{pkgrel}"]
pkgdesc = "SVG library for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/LibRsvg"
source = f"$(GNOME_SITE)/librsvg/{pkgver[:-2]}/librsvg-{pkgver}.tar.xz"
sha256 = "3728596290a8576d305d06ec8afdf473516feee9dff22e03235eac433d56824e"
# sample files may differ based on pango/freetype/harfbuzz version
options = ["!check", "!cross"]


def do_prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor(wrksrc=".")
    cargo.setup_vendor(self)


def post_patch(self):
    from cbuild.util import cargo

    cargo.clear_vendor_checksums(self, "system-deps")


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


@subpackage("librsvg-devel")
def _devel(self):
    return self.default_devel()


@subpackage("librsvg-progs")
def _progs(self):
    return self.default_progs()
