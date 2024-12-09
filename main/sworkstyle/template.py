pkgname = "sworkstyle"
pkgver = "1.3.5"
pkgrel = 1
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Map workspace names to icons for sway"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/Lyr-7D1h/swayest_workstyle"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "cee6b56c85c15d80200a2ccac5522ec65127dad4f44c5c345b64e3cc9ebb9e15"


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "sworkstyle.user")
