pkgname = "xh"
pkgver = "0.24.1"
pkgrel = 1
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
sha256 = "c5902052c66e20fd2c0b49db14edb027f54500b502108327e17260c64a42edee"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/xh")
    self.install_link("usr/bin/xhs", "xh")
    self.install_license("LICENSE")
    self.install_man("doc/xh.1")
    self.install_completion("completions/_xh", "zsh")
    self.install_completion("completions/xh.bash", "bash")
    self.install_completion("completions/xh.fish", "fish")
    self.install_completion("completions/xh.nu", "nushell")
