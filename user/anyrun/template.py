pkgname = "anyrun"
pkgver = "0_git20240716"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "gdk-pixbuf",
    "glib-devel",
    "gtk+3-devel",
    "gtk-layer-shell-devel",
    "pango-devel",
    "rust-std",
]
pkgdesc = "Wayland native krunner-like runner"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/anyrun-org/anyrun"
source = f"{url}/archive/refs/heads/master.tar.gz"
sha256 = "bbb80457b32621b2faba708a88f2e0c7339c24d34cdd36026c85c3449ad1f7c6"
# check: no meaningful tests at all
options = ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/{pkgname}")
    self.install_license("LICENSE")
