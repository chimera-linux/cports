pkgname = "dust"
pkgver = "1.1.1"
pkgrel = 1
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Simplified du -h"
license = "Apache-2.0"
url = "https://github.com/bootandy/dust"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "98cae3e4b32514e51fcc1ed07fdbe6929d4b80942925348cc6e57b308d9c4cb0"
# tests may be disabled
options = []


if self.profile().wordsize == 32:
    broken = "requires atomic64"

if self.profile().arch != "x86_64":
    # tests will fail on kernels with larger pages due to "different sizes"
    options += ["!check"]


def pre_prepare(self):
    # the version that is in there is busted on loongarch
    self.do(
        "cargo",
        "update",
        "--package",
        "libc",
        "--precise",
        "0.2.170",
        allow_network=True,
    )


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/dust")
    self.install_man("man-page/dust.1")
    with self.pushd("completions"):
        self.install_completion("_dust", "zsh")
        self.install_completion("dust.bash", "bash")
        self.install_completion("dust.fish", "fish")
