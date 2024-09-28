pkgname = "librsvg"
pkgver = "2.59.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    f"-Dtriplet={self.profile().triplet}",
    "-Davif=enabled",
    "-Ddocs=disabled",
    "-Dintrospection=enabled",
    "-Dpixbuf=enabled",
    "-Dpixbuf-loader=enabled",
    "-Dvala=enabled",
    # disabled below
    "-Dtests=false",
]
hostmakedepends = [
    "cargo-auditable",
    "cargo-c",
    "gdk-pixbuf-devel",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "python",
    "python-docutils",
    "vala",
]
makedepends = [
    "cairo-devel",
    "dav1d-devel",
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
sha256 = "6116267c7ddabfd4daaf1c341326da0a773139a7223e885ae40ee09bd6986ef6"
# check: sample files may differ based on pango/freetype/harfbuzz version
# cross: no introspection in cross
options = ["!check", "!cross"]


def prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor(wrksrc=".")


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
