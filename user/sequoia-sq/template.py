pkgname = "sequoia-sq"
pkgver = "1.3.1"
pkgrel = 0
build_style = "cargo"
make_build_env = {"ASSET_OUT_DIR": "assets"}
hostmakedepends = ["cargo-auditable", "pkgconf", "capnproto"]
makedepends = [
    "bzip2-devel",
    "capnproto-devel",
    "nettle-devel",
    "openssl3-devel",
    "rust-std",
    "sqlite-devel",
]
pkgdesc = "Command-line frontend for Sequoia, a new OpenPGP implementation"
license = "LGPL-2.0-or-later"
url = "https://sequoia-pgp.org/projects#sq"
source = f"https://gitlab.com/sequoia-pgp/sequoia-sq/-/archive/v{pkgver}/sequoia-sq-v{pkgver}.tar.gz"
sha256 = "9f112096f413e195ec737c81abb5649604f16e1f6dbe64a8accc5bb3ad39e239"
options = ["!cross"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/sq")
    self.install_man("assets/man-pages/*.1", glob=True)

    self.install_completion("assets/shell-completions/sq.bash", "bash", "sq")
    self.install_completion("assets/shell-completions/sq.fish", "fish", "sq")
    self.install_completion("assets/shell-completions/_sq", "zsh", "sq")
