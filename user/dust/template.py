pkgname = "dust"
pkgver = "1.2.3"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Simplified du -h"
license = "Apache-2.0"
url = "https://github.com/bootandy/dust"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "424b26adfbafeac31da269ecb3f189eca09803e60fad90b3ff692cf52e0aeeee"
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
