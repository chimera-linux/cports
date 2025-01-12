pkgname = "starship"
pkgver = "1.22.1"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=battery,notify,gix-faster",
]
make_install_args = [*make_build_args]
make_check_args = [
    *make_build_args,
    # /tmp is home of the cbuild user so tests that check for /tmp/dir get ~/dir as exact path
    "--",
    "--skip=modules::directory::tests::fish_directory_config_small",
    "--skip=modules::directory::tests::fish_style_directory_config_large",
    "--skip=modules::directory::tests::highlight_git_root_dir_zero_truncation_length",
    "--skip=modules::directory::tests::truncated_directory_config_large",
]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "zlib-ng-compat-devel"]
checkdepends = ["git"]
pkgdesc = "Cross-shell prompt"
maintainer = "ttyyls <contact@behri.org>"
license = "ISC"
url = "https://starship.rs"
source = (
    f"https://github.com/starship/starship/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "5434a3d1ca16987a1dd30146c36aaa4371dbe1c7f1a7995c0cf12ab3eb9326d7"
# generates completions with host binary
options = ["!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"starship.{shell}", "w") as outf:
            self.do(
                f"target/{self.profile().triplet}/release/starship",
                "completions",
                shell,
                stdout=outf,
            )


def post_install(self):
    self.install_license("LICENSE")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"starship.{shell}", shell)
