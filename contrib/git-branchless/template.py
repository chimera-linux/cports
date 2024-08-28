pkgname = "git-branchless"
pkgver = "0.9.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["libgit2-devel", "rust-std", "sqlite-devel"]
checkdepends = ["git"]
pkgdesc = "Additional tools for Git"
maintainer = "Paul A. Patience <paul@apatience.com>"
license = "MIT OR Apache-2.0"
url = "https://github.com/arxanas/git-branchless"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "fa64dc92ec522520a6407ff61241fc1819a3093337b4e3d0f80248ae76938d43"
options = ["!cross"]


def init_check(self):
    self.env["TEST_GIT"] = "/usr/bin/git"
    self.env["TEST_GIT_EXEC_PATH"] = "/usr/libexec/git-core"


def install(self):
    self.cargo.install(wrksrc="git-branchless")
    self.install_license("LICENSE-MIT")
    self.do(
        self.chroot_cwd
        / f"target/{self.profile().triplet}/release/git-branchless",
        "install-man-pages",
        self.chroot_destdir / "usr/share/man",
    )
