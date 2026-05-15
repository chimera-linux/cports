# keep in sync with glycin
pkgname = "glycin-gtk4"
pkgver = "2.1.1"
pkgrel = 1
build_style = "meson"
prepare_after_patch = True
configure_args = [
    "-Dglycin-loaders=false",
    "-Dglycin-thumbnailer=false",
    "-Dlibglycin=false",
    "-Dlibglycin-gtk4=true",
    "-Dtests=false",
    "--libexecdir=/usr/lib",  # XXX libexecdir
]
hostmakedepends = [
    "cargo-auditable",
    "gettext",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "glycin-devel",
    "glycin-loaders-none",
    "gtk4-devel",
    "libseccomp-devel",
    "pango-devel",
    "rust-std",
]
renames = ["libglycin-gtk4"]
pkgdesc = "Sandboxed and extendable image decoding"
subdesc = "GTK4 bindings"
license = "MPL-2.0 OR LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/glycin"
source = f"$(GNOME_SITE)/glycin/{pkgver[:-2]}/glycin-{pkgver}.tar.xz"
sha256 = "8e8e92e312b14d2c5f3a047bdc5305adcb9931ef0150cf74bf526a3741e6fb32"
# gobject-introspection
options = ["!cross", "!check"]


def prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)
    # so target/release is not triple-prefixed for buildsystem integration
    del self.make_env["CARGO_BUILD_TARGET"]


@subpackage("glycin-gtk4-devel")
def _(self):
    return self.default_devel()
