pkgname = "dust"
pkgver = "1.2.4"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Simplified du -h"
license = "Apache-2.0"
url = "https://github.com/bootandy/dust"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2f6768534bd01727234e67f1dd3754c9547aa18c715f6ee52094e881ebac50e3"
# tests may be disabled
options = []


if self.profile().arch != "x86_64":
    # tests will fail on kernels with larger pages due to "different sizes"
    options += ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/dust")
    self.install_man("man-page/dust.1")
    with self.pushd("completions"):
        self.install_completion("_dust", "zsh")
        self.install_completion("dust.bash", "bash")
        self.install_completion("dust.fish", "fish")
