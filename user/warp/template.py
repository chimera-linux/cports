pkgname = "warp"
pkgver = "1.0.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "cargo-auditable",
    "desktop-file-utils",
    "gettext",
    "gtk+3-update-icon-cache",
    "itstool",
    "meson",
    "pkgconf",
]
makedepends = [
    "gst-plugins-bad-devel",
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "libadwaita-devel",
    "rust-std",
]
pkgdesc = "GTK-based magic wormhole client"
license = "GPL-3.0-only"
url = "https://gitlab.gnome.org/World/warp"
source = f"{url}/-/archive/v{pkgver}/warp-{pkgver}.tar.gz"
sha256 = "3930da738c45f423beaec00fea80122a7e26e7ec7e8e245ece3fdd0ee0ad9f29"


def post_prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(f"./build/src/{self.profile().triplet}/release/warp")
