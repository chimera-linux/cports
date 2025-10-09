pkgname = "xh"
pkgver = "0.25.0"
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
sha256 = "6145f48cbefbb2bd1aa97ebcc8528d15ada1303e6e80fdd6a4637014f0f1df1c"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/xh")
    self.install_link("usr/bin/xhs", "xh")
    self.install_license("LICENSE")
    self.install_man("doc/xh.1")
    self.install_completion("completions/_xh", "zsh")
    self.install_completion("completions/xh.bash", "bash")
    self.install_completion("completions/xh.fish", "fish")
    self.install_completion("completions/xh.nu", "nushell")
