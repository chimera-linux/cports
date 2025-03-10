pkgname = "git-absorb"
pkgver = "0.7.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["asciidoc", "cargo-auditable", "pkgconf"]
makedepends = ["libgit2-devel", "rust-std"]
checkdepends = ["git"]
pkgdesc = "Automatic git commit --fixup"
license = "BSD-3-Clause"
url = "https://github.com/tummychow/git-absorb"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "65f5b80bcb726a0c40eeda94ccb47fce7f3fc4ed16021465196a37b907083eb8"
# generates completions with host bin
options = ["!cross"]


def post_build(self):
    self.do("make", "-C", "Documentation")

    for shell in ["bash", "fish", "nushell", "zsh"]:
        with open(self.cwd / f"git-absorb.{shell}", "w") as cf:
            self.do(
                f"./target/{self.profile().triplet}/release/git-absorb",
                "--gen-completions",
                shell,
                stdout=cf,
            )


def post_install(self):
    self.install_license("LICENSE.md")
    self.install_man("Documentation/git-absorb.1")

    for shell in ["bash", "fish", "nushell", "zsh"]:
        self.install_completion(f"git-absorb.{shell}", shell)
