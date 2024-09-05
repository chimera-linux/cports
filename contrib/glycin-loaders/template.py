pkgname = "glycin-loaders"
pkgver = "1.1_beta"
pkgrel = 0
build_style = "meson"
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
    "gtk4-devel",
    "libheif-devel",
    "libjxl-devel",
    "librsvg-devel",
    "libseccomp-devel",
    "libxml2-devel",
    "pango-devel",
    "rust-std",
    "vala-devel",
]
depends = ["bubblewrap"]
checkdepends = ["bubblewrap", "gtk4-devel"]
pkgdesc = "Sandboxed and extendable image decoding"
maintainer = "triallax <triallax@tutanota.com>"
license = "MPL-2.0 OR LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/sophie-h/glycin"
source = f"$(GNOME_SITE)/glycin/{pkgver[:3]}/glycin-{pkgver.replace('_', '.')}.tar.xz"
sha256 = "fdaf62ce1bbfcdd677f73283e8a58198d61d3977921c2bb16147cf69291329ca"
# deleting CARGO_BUILD_TARGET from env breaks cross
# FIXME !check: cargo-test & cargo-test-tokio broken
#   - "test-images/images/fonts/fonts.svg"
# thread 'fonts' panicked at tests/tests.rs:216:42:
# called `Result::unwrap()` on an `Err` value: ErrorCtx { error: RemoteError(ZBus(InputOutput(Custom { kind: BrokenPipe, error: "failed to read from socket" }))), stderr: Some(""), stdout: Some("") }
options = ["!cross", "!check"]


# FIXME: broken 1888 byte /usr/share/gir-1.0/GlyGtk4-1.gir
# [21/29] Generating libglycin/GlyGtk4-1.gir with a custom command (wrapped by meson to set env)
# Package libglycin-1 was not found in the pkg-config search path.
# Perhaps you should add the directory containing `libglycin-1.pc'
# to the PKG_CONFIG_PATH environment variable
# Package 'libglycin-1' not found


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)
    # so target/release is not triple-prefixed for buildsystem integration
    del self.make_env["CARGO_BUILD_TARGET"]


@subpackage("glycin-loaders-devel")
def _(self):
    return self.default_devel()
