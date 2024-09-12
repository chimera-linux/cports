pkgname = "librsvg"
pkgver = "2.58.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-introspection",
    "--enable-vala",
    "--disable-static",
    "--disable-gtk-doc",
]
hostmakedepends = [
    "automake",
    "cargo",
    "gdk-pixbuf-devel",
    "glib-devel",
    "gobject-introspection",
    "pkgconf",
    "python",
    "python-docutils",
    "slibtool",
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
provides = [self.with_pkgver("gdk-pixbuf-loader-svg")]
pkgdesc = "SVG library for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/LibRsvg"
source = f"$(GNOME_SITE)/librsvg/{pkgver[:-2]}/librsvg-{pkgver}.tar.xz"
sha256 = "296e3760d2347d0767c3e291dec962ab36baecd25c4898c6e8150a731f967c7b"
# sample files may differ based on pango/freetype/harfbuzz version
options = ["!check", "!cross"]


def prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor(wrksrc=".")


def post_patch(self):
    from cbuild.util import cargo

    cargo.clear_vendor_checksums(self, "system-deps")


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


@subpackage("librsvg-devel")
def _(self):
    return self.default_devel()


@subpackage("librsvg-progs")
def _(self):
    return self.default_progs()
