pkgname = "glycin-loaders"
pkgver = "1.0.1"
pkgrel = 3
build_style = "meson"
hostmakedepends = [
    "cargo-auditable",
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "libheif-devel",
    "libjxl-devel",
    "libseccomp-devel",
    "libxml2-devel",
    "pango-devel",
    "rust-std",
]
depends = ["bubblewrap"]
checkdepends = ["bubblewrap", "gtk4-devel"]
pkgdesc = "Sandboxed and extendable image decoding"
maintainer = "triallax <triallax@tutanota.com>"
license = "MPL-2.0 OR LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/sophie-h/glycin"
source = (
    f"$(GNOME_SITE)/glycin-loaders/{pkgver[:-2]}/glycin-loaders-{pkgver}.tar.xz"
)
sha256 = "d0f022462ff555856e85ea940474470bb36b37c9ffcbcba63a03fe5e954370cf"
# deleting CARGO_BUILD_TARGET from env breaks cross
options = ["!cross"]


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)
    # so target/release is not triple-prefixed for buildsystem integration
    del self.make_env["CARGO_BUILD_TARGET"]
