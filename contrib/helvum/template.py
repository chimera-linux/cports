pkgname = "helvum"
pkgver = "0.5.1"
pkgrel = 0
build_style = "meson"
configure_args = ["--buildtype=release"]
hostmakedepends = ["meson", "ninja", "cargo", "pkgconf", "desktop-file-utils"]
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
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "d4f5cc0c3a70a91edfc816f12a10426dadd9ca74ea82662e2df5e6c4eb31d8ca"


def post_patch(self):
    from cbuild.util import cargo

    self.cargo = cargo.Cargo(self, wrksrc=".")
    self.cargo.vendor()
    cargo.setup_vendor(self)
