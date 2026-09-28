pkgname = "sequoia-sq"
pkgver = "1.4.1"
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
sha256 = "d6c1fd6454b4f469913ab22de4fc6ec349f6effa1bd0423a4f68d868dfbbee39"
options = ["!cross"]


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "sq"))
    self.install_man("assets/man-pages/*.1", glob=True)

    self.install_completion("assets/shell-completions/sq.bash", "bash", "sq")
    self.install_completion("assets/shell-completions/sq.fish", "fish", "sq")
    self.install_completion("assets/shell-completions/_sq", "zsh", "sq")
