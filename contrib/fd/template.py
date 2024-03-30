pkgname = "fd"
pkgver = "9.0.0"
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
    "306d7662994e06e23d25587246fa3fb1f528579e42a84f5128e75feec635a370",
    "069e2d58127ddd944c03a2684ad79f72e3f9bd3e0d2642c36adc5b367c134592",
]


def post_install(self):
    self.install_license("LICENSE-MIT")
    self.install_man("extra/fd.1")
    self.install_completion("extra/autocomplete/fd.bash", "bash", "fd")
    self.install_completion("extra/autocomplete/fd.fish", "fish", "fd")
    self.install_completion("extra/autocomplete/_fd", "zsh", "fd")
