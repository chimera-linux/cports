pkgname = "git-cliff"
pkgver = "2.2.0"
pkgrel = 0
build_style = "cargo"
make_check_args = [
    "--",
    "--skip=repo::test::git_log",
    "--skip=repo::test::git_tags",
    "--skip=repo::test::git_upstream_remote",
]
hostmakedepends = ["cargo", "pkgconf"]
makedepends = ["libgit2-devel"]
pkgdesc = "Changelog generator for conventional commits"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0 OR MIT"
url = "https://github.com/orhun/git-cliff"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d89af1c654e63ce2f6c09cd63d691bf531f0ccd76b670316cc71529f1d4eaccb"
# generates manpages/completions with host bins
options = ["!cross"]


def post_build(self):
    self.do(
        f"target/{self.profile().triplet}/release/git-cliff-mangen",
        env={"OUT_DIR": "."},
    )
    self.do(
        f"target/{self.profile().triplet}/release/git-cliff-completions",
        env={"OUT_DIR": "."},
    )


def do_install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/git-cliff")
    self.install_man("git-cliff.1")
    self.install_completion("git-cliff.bash", "bash")
    self.install_completion("git-cliff.fish", "fish")
    self.install_completion("_git-cliff", "zsh")
    self.install_license("LICENSE-MIT")
