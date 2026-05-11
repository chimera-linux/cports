pkgname = "helvum"
pkgver = "0.6.1"
pkgrel = 0
build_style = "meson"
configure_args = ["--buildtype=release"]
hostmakedepends = [
    "cargo-auditable",
    "desktop-file-utils",
    "gtk+3-update-icon-cache",
    "meson",
    "ninja",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "gtk4-devel",
    "libadwaita-devel",
    "pipewire-devel",
    "rust-std",
]
pkgdesc = "GTK patchbay for PipeWire"
license = "GPL-3.0-only"
url = "https://gitlab.freedesktop.org/pipewire/helvum"
source = f"{url}/-/archive/{pkgver}/helvum-{pkgver}.tar.bz2"
sha256 = "9cc26e7031ab2fb7d54c6125a6a32736ee5b22e5604dc88ed533f2b6fafa8a6c"

if self.profile().wordsize == 32:
    broken = "expected *mut i64, found *mut i32"

if self.profile().arch in ["loongarch64"]:
    broken = "old nix crate, can't update"


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(f"./build/src/{self.profile().triplet}/release/helvum")
