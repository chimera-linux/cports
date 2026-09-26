pkgname = "video-trimmer"
pkgver = "26.03.1"
pkgrel = 0
build_style = "meson"
configure_args = ["--buildtype=release"]
hostmakedepends = [
    "blueprint-compiler",
    "cargo-auditable",
    "desktop-file-utils",
    "gettext",
    "meson",
    "ninja",
    "pkgconf",
]
makedepends = [
    "libadwaita-devel",
    "rust-std",
]
pkgdesc = "Simple graphical video trimmer"
license = "GPL-3.0-only"
url = "https://gitlab.gnome.org/YaLTeR/video-trimmer"
source = f"{url}/-/archive/v{pkgver}/{pkgname}-v{pkgver}.tar.gz"
sha256 = "f840e22e5b9fa6fc82d522138dc183f5b5840b21e78b7b5843a3d889a2105bef"


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()
