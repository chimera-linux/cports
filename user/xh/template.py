pkgname = "xh"
pkgver = "0.26.2"
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
sha256 = "61a88a5b3beac225b75a11d6ed32659af78db7ff29c825def0ab7f4a2906cbd7"


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "xh"))
    self.install_link("usr/bin/xhs", "xh")
    self.install_license("LICENSE")
    self.install_man("doc/xh.1")
    self.install_completion("completions/_xh", "zsh")
    self.install_completion("completions/xh.bash", "bash")
    self.install_completion("completions/xh.fish", "fish")
    self.install_completion("completions/xh.nu", "nushell")
