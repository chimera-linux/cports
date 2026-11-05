pkgname = "fd"
pkgver = "10.5.1"
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
    "3ea70c258d3390a601b436b6f4c545e3a944ff3de44c8ee5542c05588e337032",
    "f6c95edb190c241df6fddc815a5bab4051444993ac5d92ddc6eec0e0dc2342c7",
]


def post_install(self):
    self.install_license("LICENSE-MIT")
    self.install_man("extra/fd.1")
    self.install_completion("extra/autocomplete/fd.bash", "bash")
    self.install_completion("extra/autocomplete/fd.fish", "fish")
    self.install_completion("extra/autocomplete/_fd", "zsh")
