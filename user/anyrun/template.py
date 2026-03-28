pkgname = "anyrun"
pkgver = "25.12.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "cairo-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "gtk4-devel",
    "gtk4-layer-shell-devel",
    "pango-devel",
]
depends = ["anyrun-provider"]
pkgdesc = "Wayland native, highly customizable runner"
license = "GPL-3.0-or-later"
url = "https://github.com/anyrun-org/anyrun"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4213a2f65fd6139829128d3c7a7f4b54fec3181f8d549e212021341dd10c3d50"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/{pkgname}")
    self.install_license("LICENSE")

    self.install_file(
        "target/release/*.so", "usr/lib/anyrun/plugins/", glob=True
    )
    self.install_file("examples/config.ron", "etc/anyrun")
