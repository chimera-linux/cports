# keep in sync with glycin
pkgname = "glycin-loaders"
pkgver = "2.2.6"
pkgrel = 0
build_style = "meson"
prepare_after_patch = True
configure_args = [
    "-Dglycin-loaders=true",
    "-Dglycin-thumbnailer=false",
    "-Dlibglycin=false",
    "-Dlibglycin-gtk4=false",
    "-Dloaders=glycin-heif,glycin-jxl,glycin-svg",
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
    "glycin-devel",
    "glycin-loaders-none",
    "libheif-devel",
    "libjxl-devel",
    "librsvg-devel",
    "libseccomp-devel",
    "pango-devel",
    "rust-std",
]
depends = ["bubblewrap"]
pkgdesc = "Sandboxed and extendable image decoding"
subdesc = "additional loaders"
license = "MPL-2.0 OR LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/glycin"
source = f"$(GNOME_SITE)/glycin/{pkgver[:-2]}/glycin-{pkgver}.tar.xz"
sha256 = "6a114aa1117ec2d7bd578c8cefd235d993304dedfd1a62575dc31be9a146b791"
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
