pkgname = "sworkstyle"
pkgver = "1.3.6"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["dinit-chimera", "rust-std"]
pkgdesc = "Map workspace names to icons for sway"
license = "MIT"
url = "https://github.com/Lyr-7D1h/swayest_workstyle"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "dc6bb5b63a568a0c19e4477e06a683ddcf208213af92f47ae7fda175b6f77fb9"


def pre_prepare(self):
    # the version that is in there is busted on loongarch
    self.do(
        "cargo",
        "update",
        "--package",
        "libc",
        "--precise",
        "0.2.170",
        allow_network=True,
    )


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "sworkstyle.user")
