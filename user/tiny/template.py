pkgname = "tiny"
pkgver = "0.13.0"
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
makedepends = ["dbus-devel", "openssl3-devel", "rust-std"]
pkgdesc = "Terminal IRC client"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT"
url = "https://github.com/osa1/tiny"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "599697fa736d7500b093566a32204691093bd16abd76f43a76b761487a7c584c"


def install(self):
    self.cargo.install(wrksrc="crates/tiny")
    self.install_license("LICENSE")
