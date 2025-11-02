pkgname = "librsvg"
pkgver = "2.61.2"
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
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/LibRsvg"
source = f"$(GNOME_SITE)/librsvg/{pkgver[:-2]}/librsvg-{pkgver}.tar.xz"
sha256 = "4644d83623dd61cc4479c2b3c372e1da2b281552ebc90035c8d1ac502eb1dc00"
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
