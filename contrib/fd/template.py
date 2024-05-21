pkgname = "fd"
pkgver = "10.1.0"
pkgrel = 0
build_style = "cargo"
# disable the default use-jemalloc and completions features
make_build_args = ["--no-default-features"]
make_install_args = ["--no-default-features"]
make_check_args = ["--no-default-features"]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Simple, fast and user-friendly alternative to find"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT OR Apache-2.0"
url = "https://github.com/sharkdp/fd"
source = [
    f"{url}/archive/v{pkgver}.tar.gz",
    # release tarball is used to acquire completions without having to run the binary
    f"{url}/releases/download/v{pkgver}/fd-v{pkgver}-x86_64-unknown-linux-musl.tar.gz",
]
source_paths = [".", "extra"]
sha256 = [
    "ee4b2403388344ff60125c79ff25b7895a170e7960f243ba2b5d51d2c3712d97",
    "f8fa73aa005e71598c1cdbb03ae6979fd016d5a8aaf92ee84ed6f8f186c58ead",
]


def post_install(self):
    self.install_license("LICENSE-MIT")
    self.install_man("extra/fd.1")
    self.install_completion("extra/autocomplete/fd.bash", "bash", "fd")
    self.install_completion("extra/autocomplete/fd.fish", "fish", "fd")
    self.install_completion("extra/autocomplete/_fd", "zsh", "fd")
