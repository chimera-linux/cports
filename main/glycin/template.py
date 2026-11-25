# keep in sync with glycin-gtk4 and glycin-loaders
pkgname = "glycin"
pkgver = "2.2.6"
pkgrel = 0
build_style = "meson"
prepare_after_patch = True
configure_args = [
    "-Dlibglycin-gtk4=false",
    # we bundle dependency-free loader as that's needed for gdk-pixbuf
    "-Dloaders=glycin-image-rs",
    "-Dtests=false",
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
    "cairo-devel",
    "lcms2-devel",
    "libseccomp-devel",
    "pango-devel",
    "rust-std",
]
depends = ["bubblewrap", "virtual:glycin-loaders!glycin-loaders-none"]
checkdepends = [*depends]
renames = ["libglycin"]
pkgdesc = "Sandboxed and extendable image decoding"
license = "MPL-2.0 OR LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/glycin"
source = f"$(GNOME_SITE)/glycin/{pkgver[:-2]}/glycin-{pkgver}.tar.xz"
sha256 = "6a114aa1117ec2d7bd578c8cefd235d993304dedfd1a62575dc31be9a146b791"
# gobject-introspection
# check: for some divine reason, it always passes locally and never on the builders (??)
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


@split("devel")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libglycin-devel")]

    return self.default_devel()


@split("loaders-none")
def _(self):
    self.subdesc = "no additional loaders"
    self.depends = [self.parent]
    self.provides = ["glycin-loaders=0"]
    self.options = ["empty"]

    return []
