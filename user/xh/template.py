pkgname = "xh"
pkgver = "0.25.3"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=native-tls",
]
make_check_args = [*make_build_args]
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "oniguruma-devel",
    "openssl3-devel",
    "rust-std",
]
pkgdesc = "Tool for sending HTTP requests"
license = "MIT"
url = "https://github.com/ducaale/xh"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ba331c33dc5d222f43cc6ad9f602002817772fd52ae28541976db49f34935ae3"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/xh")
    self.install_link("usr/bin/xhs", "xh")
    self.install_license("LICENSE")
    self.install_man("doc/xh.1")
    self.install_completion("completions/_xh", "zsh")
    self.install_completion("completions/xh.bash", "bash")
    self.install_completion("completions/xh.fish", "fish")
    self.install_completion("completions/xh.nu", "nushell")
