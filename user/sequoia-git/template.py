pkgname = "sequoia-git"
pkgver = "0.6.0"
pkgrel = 0
build_style = "cargo"
make_build_env = {"ASSET_OUT_DIR": "assets"}
make_check_env = {"TARGET": self.profile.triplet, "NO_FAKETIME": "1"}
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "bzip2-devel",
    "libgit2-devel",
    "nettle-devel",
    "openssl3-devel",
    "rust-std",
    "sqlite-devel",
]
checkdepends = ["git", "gnupg"]
pkgdesc = "Tool to verify git commit signatures based on a policy"
license = "LGPL-2.0-or-later"
url = "https://gitlab.com/sequoia-pgp/sequoia-git"
source = f"{url}/-/archive/v{pkgver}/sequoia-git-v{pkgver}.tar.gz"
sha256 = "8c54cc01b3ef9a51b432e1b2c0ce29e5b9c10684ce1b8e5bb1f5d8f247916120"
options = ["!cross"]


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "sq-git"))

    self.install_man("assets/man-pages/*.1", glob=True)
    self.install_completion(
        "assets/shell-completions/sq-git.bash", "bash", "sq-git"
    )
    self.install_completion(
        "assets/shell-completions/sq-git.fish", "fish", "sq-git"
    )
    self.install_completion("assets/shell-completions/_sq-git", "zsh", "sq-git")
