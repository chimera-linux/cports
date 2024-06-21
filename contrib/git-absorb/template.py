pkgname = "git-absorb"
pkgver = "0.6.13"
pkgrel = 2
build_style = "cargo"
prepare_after_patch = True
hostmakedepends = ["asciidoc", "cargo-auditable", "pkgconf"]
makedepends = ["libgit2-devel"]
pkgdesc = "Automatic git commit --fixup"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "BSD-3-Clause"
url = "https://github.com/tummychow/git-absorb"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "5646857dd764d0a486405e777b3ec4e919511abc96bd0e02e71ec9e94d151115"
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
