pkgname = "openpgp-card-tools"
pkgver = "0.11.3"
pkgrel = 1
build_style = "cargo"
prepare_after_patch = True
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "pcsc-lite-devel"]
depends = ["ccid"]
pkgdesc = "CLI tool for inspecting, configuring and using OpenPGP cards"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0 OR MIT"
url = "https://codeberg.org/openpgp-card/openpgp-card-tools"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "083fe2e127baaee5dc799274d7208db5a3b7debde433f762263b8e4912af1d3c"
# generates completions using host binary
options = ["!cross"]


def post_build(self):
    self.do(
        f"target/{self.profile().triplet}/release/oct",
        "completions",
        "completions",
    )


def post_install(self):
    self.install_license("LICENSES/MIT.txt")
    with self.pushd("completions"):
        self.install_completion("oct.bash", "bash", "oct")
        self.install_completion("oct.fish", "fish", "oct")
        self.install_completion("_oct", "zsh", "oct")
        self.install_completion("oct.nu", "nushell", "oct")
