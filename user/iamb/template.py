pkgname = "iamb"
pkgver = "0.13.1"
pkgrel = 2
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features",
    "desktop",
    "--bin",
    "iamb",
]
make_install_args = [*make_build_args]
make_check_args = [*make_build_args]
hostmakedepends = [
    "cargo-auditable",
    "rust-std",
]
makedepends = [
    "sqlite-devel",
]
depends = [
    "sqlite",
]
pkgdesc = "TUI Matrix client with Vi-like controls"
license = "Apache-2.0"
url = "https://iamb.chat"
source = f"https://github.com/ulyssa/iamb/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8e919c19ef90f328d20e6e46720a26f0dea6e61901b8180fedbbacb473f131f1"


def post_install(self):
    self.install_man("docs/iamb.1")
    self.install_man("docs/iamb.5")

    self.install_files("themes", "usr/share/iamb")

    self.install_file("iamb.desktop", "usr/share/applications")
    self.install_file("config.full.toml", "usr/share/examples/iamb")
    self.install_file("docs/iamb.svg", "usr/share/icons/hicolor/scalable/apps")
    self.install_file("docs/iamb.metainfo.xml", "usr/share/metainfo")
