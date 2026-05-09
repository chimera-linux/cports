pkgname = "openpgp-card-tools"
pkgver = "0.11.12"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "pcsc-lite-devel", "dbus-devel"]
depends = ["ccid"]
pkgdesc = "CLI tool for inspecting, configuring and using OpenPGP cards"
license = "Apache-2.0 OR MIT"
url = "https://codeberg.org/openpgp-card/openpgp-card-tools"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "f21ea3b67cf051fc74dd8a7f11ee4d9445f416ad566e479140bb51f28ce6ab75"
# generates completions using host binary
options = ["!cross"]


def post_build(self):
    self.do(
        f"target/{self.profile().triplet}/release/oct",
        env={"OCT_MANPAGE_OUTPUT_DIR": "man"},
    )
    self.do(
        f"target/{self.profile().triplet}/release/oct",
        env={"OCT_COMPLETION_OUTPUT_DIR": "completions"},
    )


def post_install(self):
    self.install_license("LICENSES/MIT.txt")
    self.install_man("man/*.1", glob=True)
    with self.pushd("completions"):
        self.install_completion("oct.bash", "bash", "oct")
        self.install_completion("oct.fish", "fish", "oct")
        self.install_completion("_oct", "zsh", "oct")
        self.install_completion("oct.nu", "nushell", "oct")
