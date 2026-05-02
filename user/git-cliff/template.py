pkgname = "git-cliff"
pkgver = "2.13.1"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=integrations",
]
make_install_args = [*make_build_args]
make_check_args = [
    *make_build_args,
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
checkdepends = ["git"]
pkgdesc = "Changelog generator for conventional commits"
license = "Apache-2.0 OR MIT"
url = "https://github.com/orhun/git-cliff"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3dd3138a009ade1085dd2f001f836c2bb406462a99512dbcb573bda1f2166274"
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
