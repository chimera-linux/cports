pkgname = "satty"
pkgver = "0.12.0"
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
sha256 = "42403b36e7babe245de2bebc78d4bebab68aeaa4594b28bb9d83f44808e52920"
# no tests defined
options = ["!check"]


def post_install(self):
    self.install_file("satty.desktop", "usr/share/applications")
    self.install_file(
        "assets/satty.svg", "usr/share/icons/hicolor/scalable/apps"
    )
    self.install_completion("completions/satty.bash", "bash")
    self.install_completion("completions/satty.fish", "fish")
    self.install_completion("completions/_satty", "zsh")
