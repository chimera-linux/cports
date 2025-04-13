pkgname = "loupe"
pkgver = "48.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "cargo-auditable",
    "desktop-file-utils",
    "gettext",
    "glib",
    "gtk+3-update-icon-cache",
    "itstool",
    "meson",
    "pkgconf",
]
makedepends = [
    "gtk4-devel",
    "lcms2-devel",
    "libadwaita-devel",
    "libgweather-devel",
    "libseccomp-devel",
    "rust-std",
]
depends = ["glycin-loaders"]
pkgdesc = "GNOME image viewer"
license = "GPL-3.0-or-later"
url = "https://apps.gnome.org/Loupe"
source = f"$(GNOME_SITE)/loupe/{pkgver[:-2]}/loupe-{pkgver}.tar.xz"
sha256 = "10713d3e96789d077ae7d3389452a5f6c397ddf43a50c071cbfe2d12725970de"
# Runs `cargo test` but doesn't actually have any rust tests for that to execute
options = ["!check"]


def prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()
    cargo.clear_vendor_checksums(self, "zvariant")


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(f"./build/src/{self.profile().triplet}/release/loupe")
