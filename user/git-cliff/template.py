pkgname = "git-cliff"
pkgver = "2.8.0"
pkgrel = 0
build_style = "cargo"
prepare_after_patch = True
make_check_args = [
    "--",
    "--skip=repo::test::commit_search",
    "--skip=repo::test::get_latest_commit",
    "--skip=repo::test::get_latest_tag",
    "--skip=repo::test::git_log",
    "--skip=repo::test::git_tags",
    "--skip=repo::test::git_upstream_remote",
    "--skip=repo::test::includes_root_commit",
    "--skip=repo::test::open_jujutsu_repo",
    "--skip=repo::test::resolves_existing_tag_with_name_and_message",
    "--skip=repo::test::resolves_tag_when_no_tags_exist",
    "--skip=repo::test::test_should_retain_commit",
]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["libgit2-devel", "rust-std", "zstd-devel"]
pkgdesc = "Changelog generator for conventional commits"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0 OR MIT"
url = "https://github.com/orhun/git-cliff"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "dfcf7b7d903c6479e58c8e7594364d67ce59e3e50351b3277eb33482a783418d"
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


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/git-cliff")
    self.install_man("git-cliff.1")
    self.install_completion("git-cliff.bash", "bash")
    self.install_completion("git-cliff.fish", "fish")
    self.install_completion("_git-cliff", "zsh")
    self.install_license("LICENSE-MIT")
