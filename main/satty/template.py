pkgname = "satty"
pkgver = "0.16.0"
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
sha256 = "36ffbea973fd844d92998f1d5aed53c779692e956ed07490d324812223eab4bd"
# no tests defined
options = ["!check"]


def install(self):
    self.install_bin(f"./target/{self.profile().triplet}/release/satty")
    self.install_file("satty.desktop", "usr/share/applications")
    self.install_file(
        "assets/satty.svg", "usr/share/icons/hicolor/scalable/apps"
    )
    self.install_completion("completions/satty.bash", "bash")
    self.install_completion("completions/satty.fish", "fish")
    self.install_completion("completions/_satty", "zsh")
