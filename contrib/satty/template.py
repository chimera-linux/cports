pkgname = "satty"
pkgver = "0.13.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "fontconfig-devel",
    "gtk4-devel",
    "libadwaita-devel",
    "libepoxy-devel",
    "rust-std",
]
pkgdesc = "Screenshot annotation tool"
maintainer = "ttyyls <contact@behri.org>"
license = "MPL-2.0"
url = "https://github.com/gabm/Satty"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7903b9886894c86983089994e9abb864ad2c8aacca01cf66a9536de619982052"
# no tests defined
options = ["!check"]


def do_install(self):
    self.install_bin(f"./target/{self.profile().triplet}/release/satty")
    self.install_file("satty.desktop", "usr/share/applications")
    self.install_file(
        "assets/satty.svg", "usr/share/icons/hicolor/scalable/apps"
    )
    self.install_completion("completions/satty.bash", "bash")
    self.install_completion("completions/satty.fish", "fish")
    self.install_completion("completions/_satty", "zsh")
