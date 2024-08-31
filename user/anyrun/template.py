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
source = f"{url}/archive/c6101a31a80b51e32e96f6a77616b609770172e0.tar.gz"
sha256 = "1bcbba5301280249966fbcdd9e2d2fdec3586a3bade1c8bd8904e1d77fb1492f"
# check: no meaningful tests at all
options = ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/{pkgname}")
    self.install_license("LICENSE")
