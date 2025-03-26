pkgname = "sequoia-git"
pkgver = "0.4.0"
pkgrel = 0
build_style = "cargo"
prepare_after_patch = True
make_check_env = {"TARGET": self.profile().triplet, "NO_FAKETIME": "1"}
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
sha256 = "8148f94e107371454988ff897973dfb5f6d2b8c021565011a34728faf9e33d75"
options = ["!cross"]


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
    self.install_bin(f"target/{self.profile().triplet}/release/sq-git")
    self.install_man(
        f"target/{self.profile().triplet}/release/build/sequoia-git-*/out/man-pages/*.1",
        glob=True,
    )

    self.install_completion("completions/sq-git.bash", "bash", "sq-git")
    self.install_completion("completions/sq-git.fish", "fish", "sq-git")
    self.install_completion("completions/_sq-git", "zsh", "sq-git")
