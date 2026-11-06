pkgname = "dust"
pkgver = "1.2.7"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Simplified du -h"
license = "Apache-2.0"
url = "https://github.com/bootandy/dust"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "923a2eed637d2ea5f4ad5f820b6f87cc6e0081cfa4bc5ed1fe09278dd74db963"
# tests may be disabled
options = []


if self.profile.arch != "x86_64":
    # tests will fail on kernels with larger pages due to "different sizes"
    options += ["!check"]


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "dust"))
    self.install_man("man-page/dust.1")
    with self.pushd("completions"):
        self.install_completion("_dust", "zsh")
        self.install_completion("dust.bash", "bash")
        self.install_completion("dust.fish", "fish")
