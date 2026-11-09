pkgname = "fd"
pkgver = "10.5.2"
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
    "8991b6504cac33c00528050622dfe3f2a0db1be1a6faf99f69b46d1a8f737dc5",
    "7e2d07fa2b8807642aaec67b7e2972a9fbe4db26fcb340a7372392db42b26694",
]


def post_install(self):
    self.install_license("LICENSE-MIT")
    self.install_man("extra/fd.1")
    self.install_completion("extra/autocomplete/fd.bash", "bash")
    self.install_completion("extra/autocomplete/fd.fish", "fish")
    self.install_completion("extra/autocomplete/_fd", "zsh")
