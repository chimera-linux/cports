pkgname = "dust"
pkgver = "1.1.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Simplified du -h"
license = "Apache-2.0"
url = "https://github.com/bootandy/dust"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "31da99483ee6110d43ed5e7c56a59f40f33b389e45d09d91fca022b42d442040"


if self.profile().wordsize == 32:
    broken = "requires atomic64"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/dust")
    self.install_man("man-page/dust.1")
    with self.pushd("completions"):
        self.install_completion("_dust", "zsh")
        self.install_completion("dust.bash", "bash")
        self.install_completion("dust.fish", "fish")
