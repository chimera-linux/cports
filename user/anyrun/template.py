pkgname = "anyrun"
pkgver = "26.10.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "cairo-devel",
    "gtk4-devel",
    "gtk4-layer-shell-devel",
    "pango-devel",
]
depends = ["anyrun-provider"]
pkgdesc = "Customizable runner program for Wayland"
license = "GPL-3.0-or-later"
url = "https://github.com/anyrun-org/anyrun"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d7c32956b97654340f64f532177bc255c27d448382495f16a364986bbad03188"


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "anyrun"))

    # PLUGIN_PATHS in anyrun-provider
    self.install_file(
        cargo.target_path(self, "*.so"),
        "usr/lib/anyrun",
        glob=True,
    )

    # configure this for yourself in ~/.config
    self.install_file("examples/config.ron", "usr/share/examples/anyrun")
