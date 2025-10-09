pkgname = "fd"
pkgver = "10.3.0"
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
    "2edbc917a533053855d5b635dff368d65756ce6f82ddefd57b6c202622d791e9",
    "2b6bfaae8c48f12050813c2ffe1884c61ea26e750d803df9c9114550a314cd14",
]


def post_install(self):
    self.install_license("LICENSE-MIT")
    self.install_man("extra/fd.1")
    self.install_completion("extra/autocomplete/fd.bash", "bash")
    self.install_completion("extra/autocomplete/fd.fish", "fish")
    self.install_completion("extra/autocomplete/_fd", "zsh")
