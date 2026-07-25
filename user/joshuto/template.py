pkgname = "joshuto"
pkgver = "0.9.9"
pkgrel = 0
build_style = "cargo"
# needs bundled libgit version
make_env = {"LIBGIT2_NO_VENDOR": "0"}
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "zlib-ng-devel"]
pkgdesc = "Ranger-like terminal file manager"
license = "LGPL-3.0-only"
url = "https://github.com/kamiyaa/joshuto"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "85a230183f7478dee7c29229d78313ee07b759e596e19292acf024d2e5735efa"
# cross: uses native binary to generate completions
options = ["!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"joshuto.{shell}", "w") as cf:
            self.do(
                f"./target/{self.profile().triplet}/release/joshuto",
                "completions",
                shell,
                stdout=cf,
            )


def post_install(self):
    self.install_license("LICENSE")
    self.install_completion("joshuto.bash", "bash", "joshuto")
    self.install_completion("joshuto.fish", "fish", "joshuto")
    self.install_completion("joshuto.zsh", "zsh", "joshuto")
