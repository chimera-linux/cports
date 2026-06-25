pkgname = "rmpc"
pkgver = "0.11.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "rust-std",
]
pkgdesc = "TUI MPD client with album art support"
license = "BSD-3-Clause"
url = "https://github.com/mierak/rmpc"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "930019066228d18e9530a8c0d77f10e231ab5efbbbca73b331efcd6fbb47557d"
hardening = ["vis", "cfi"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/rmpc")
    self.install_license("LICENSE")

    self.install_completion("target/completions/rmpc.bash", "bash", "rmpc")
    self.install_completion("target/completions/rmpc.fish", "fish", "rmpc")
    self.install_completion("target/completions/_rmpc", "zsh", "rmpc")

    self.install_man("target/man/rmpc.1")
