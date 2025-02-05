pkgname = "sequoia-git"
pkgver = "0.1.0"
pkgrel = 3
build_style = "cargo"
prepare_after_patch = True
make_check_env = {"TARGET": self.profile().triplet}
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
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "LGPL-2.0-or-later"
url = "https://gitlab.com/sequoia-pgp/sequoia-git"
source = f"{url}/-/archive/v{pkgver}/sequoia-git-v{pkgver}.tar.gz"
sha256 = "c1f7d2647538f3335dab8862a9c4b78bac8c41bb22a3917ec45989849fd035dd"
options = ["!cross"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/sq-git")
    self.install_man("man/*.1", glob=True)

    self.install_completion("completions/sq-git.bash", "bash", "sq-git")
    self.install_completion("completions/sq-git.fish", "fish", "sq-git")
    self.install_completion("completions/_sq-git", "zsh", "sq-git")
