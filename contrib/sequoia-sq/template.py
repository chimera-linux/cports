pkgname = "sequoia-sq"
pkgver = "0.35.0"
pkgrel = 0
build_style = "cargo"
make_build_env = {"ASSET_OUT_DIR": "assets"}
hostmakedepends = ["cargo-auditable", "pkgconf", "capnproto"]
makedepends = [
    "bzip2-devel",
    "capnproto-devel",
    "nettle-devel",
    "openssl-devel",
    "rust-std",
    "sqlite-devel",
]
pkgdesc = "Command-line frontend for Sequoia, a new OpenPGP implementation"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "LGPL-2.0-or-later"
url = "https://sequoia-pgp.org/projects#sq"
source = f"https://gitlab.com/sequoia-pgp/sequoia-sq/-/archive/v{pkgver}/sequoia-sq-v{pkgver}.tar.gz"
sha256 = "0b16bb4dcd7b85eb1292dfe4b22dfa3c0df44bae1e84859e91aadfee80b08bec"
options = ["!cross"]


def do_install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/sq")
    self.install_man("assets/man-pages/*.1", glob=True)

    self.install_completion("assets/shell-completions/sq.bash", "bash", "sq")
    self.install_completion("assets/shell-completions/sq.fish", "fish", "sq")
    self.install_completion("assets/shell-completions/_sq", "zsh", "sq")
