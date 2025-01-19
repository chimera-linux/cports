pkgname = "fd"
pkgver = "10.2.0"
pkgrel = 1
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
    "73329fe24c53f0ca47cd0939256ca5c4644742cb7c14cf4114c8c9871336d342",
    "d9bfa25ec28624545c222992e1b00673b7c9ca5eb15393c40369f10b28f9c932",
]


def post_install(self):
    self.install_license("LICENSE-MIT")
    self.install_man("extra/fd.1")
    self.install_completion("extra/autocomplete/fd.bash", "bash")
    self.install_completion("extra/autocomplete/fd.fish", "fish")
    self.install_completion("extra/autocomplete/_fd", "zsh")
