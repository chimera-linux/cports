pkgname = "fd"
pkgver = "10.5.0"
pkgrel = 0
build_style = "cargo"
# disable the default use-jemalloc and completions features
make_build_args = ["--no-default-features"]
make_install_args = ["--no-default-features"]
make_check_args = ["--no-default-features"]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Simple, fast and user-friendly alternative to find"
license = "MIT OR Apache-2.0"
url = "https://github.com/sharkdp/fd"
source = [
    f"{url}/archive/v{pkgver}.tar.gz",
    # release tarball is used to acquire completions without having to run the binary
    f"{url}/releases/download/v{pkgver}/fd-v{pkgver}-x86_64-unknown-linux-musl.tar.gz",
]
source_paths = [".", "extra"]
sha256 = [
    "e6d9e90730bf316101691e49d59cc02565278dc3779d33a77423801569484851",
    "761c72dc8e120d85b22292063be8a796e2eeb20eb3e4f38b8fa2343ccf3514a7",
]


def post_install(self):
    self.install_license("LICENSE-MIT")
    self.install_man("extra/fd.1")
    self.install_completion("extra/autocomplete/fd.bash", "bash")
    self.install_completion("extra/autocomplete/fd.fish", "fish")
    self.install_completion("extra/autocomplete/_fd", "zsh")
