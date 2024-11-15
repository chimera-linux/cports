pkgname = "tiny"
pkgver = "0.12.0"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features",
    "tls-native,desktop-notifications",
    "--bin",
    "tiny",
]
make_install_args = [*make_build_args]
make_check_args = [*make_build_args]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["dbus-devel", "openssl-devel", "rust-std"]
pkgdesc = "Terminal IRC client"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT"
url = "https://github.com/osa1/tiny"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "95406a234fe4c7013edab622970e89a5b56d4441fb5c1ec871a992fc6ee8db7a"


def install(self):
    self.cargo.install(wrksrc="crates/tiny")
    self.install_license("LICENSE")
