pkgname = "helvum"
pkgver = "0.5.1"
pkgrel = 2
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
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-3.0-only"
url = "https://gitlab.freedesktop.org/pipewire/helvum"
source = f"{url}/-/archive/{pkgver}/helvum-{pkgver}.tar.bz2"
sha256 = "d4f5cc0c3a70a91edfc816f12a10426dadd9ca74ea82662e2df5e6c4eb31d8ca"

if self.profile().wordsize == 32:
    broken = "expected *mut i64, found *mut i32"


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(f"./build/src/{self.profile().triplet}/release/helvum")
