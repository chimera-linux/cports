pkgname = "librsvg"
pkgver = "2.63.4"
pkgrel = 0
build_style = "meson"
configure_args = [
    f"-Dtriplet={self.profile.triplet}",
    # when building both (our default), rsvg/meson.build creates a special
    # rsvg-gir shared library target for gir generation, which then results
    # in the typelib containing a wrong shlib reference (librsvg-gir.so instead
    # of librsvg-2.so.2), so work aorund this by disabling static library
    "-Ddefault_library=shared",
    "-Davif=enabled",
    "-Ddocs=disabled",
    "-Dintrospection=enabled",
    "-Dpixbuf=enabled",
    "-Dpixbuf-loader=disabled",
    "-Dvala=enabled",
    # disabled below
    "-Dtests=false",
]
hostmakedepends = [
    "cargo-auditable",
    "cargo-c",
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
pkgdesc = "SVG library for GNOME"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/LibRsvg"
source = f"$(GNOME_SITE)/librsvg/{pkgver[:-2]}/librsvg-{pkgver}.tar.xz"
sha256 = "31f07d9350dad3f8964fd613c31309ac160fdef13dfac59df6fd082de78d6e8f"
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
