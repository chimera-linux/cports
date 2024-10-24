pkgname = "git-branchless"
pkgver = "0.10.0"
pkgrel = 0
build_style = "cargo"
prepare_after_patch = True
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["libgit2-devel", "rust-std", "sqlite-devel"]
checkdepends = ["git"]
pkgdesc = "Additional tools for Git"
maintainer = "Paul A. Patience <paul@apatience.com>"
license = "MIT OR Apache-2.0"
url = "https://github.com/arxanas/git-branchless"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1eb8dbb85839c5b0d333e8c3f9011c3f725e0244bb92f4db918fce9d69851ff7"
# check: test snapshots fail with libgit2 1.8
options = ["!cross", "!check"]


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
