pkgname = "sequoia-sq"
pkgver = "1.4.0"
pkgrel = 0
build_style = "cargo"
make_build_env = {"ASSET_OUT_DIR": "assets"}
# Tries to rename a file to /dev/null, passes outside bldroot
make_check_args = [
    "--",
    "--skip=integration::sq_key_generate::sq_key_generate_dev_null",
]
hostmakedepends = ["cargo-auditable", "pkgconf", "capnproto"]
makedepends = [
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
sha256 = "c856bfb0f0c94a1b8f4b72a04a6eff1e1d3d24c377cb0b1e495688e9aad8467a"
options = ["!cross"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/sq")
    self.install_man("assets/man-pages/*.1", glob=True)

    self.install_completion("assets/shell-completions/sq.bash", "bash", "sq")
    self.install_completion("assets/shell-completions/sq.fish", "fish", "sq")
    self.install_completion("assets/shell-completions/_sq", "zsh", "sq")
