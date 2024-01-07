pkgname = "git-branchless"
pkgver = "0.8.0"
pkgrel = 1
build_style = "cargo"
hostmakedepends = ["cargo"]
makedepends = ["rust-std", "sqlite-devel"]
checkdepends = ["git"]
pkgdesc = "Additional tools for Git"
maintainer = "Paul A. Patience <paul@apatience.com>"
license = "MIT OR Apache-2.0"
url = "https://github.com/arxanas/git-branchless"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f9e13d9a3de960b32fb684a59492defd812bb0785df48facc964478f675f0355"
options = ["!cross"]


def init_check(self):
    self.env["TEST_GIT"] = "/usr/bin/git"
    self.env["TEST_GIT_EXEC_PATH"] = "/usr/libexec/git-core"


def do_install(self):
    self.cargo.install(wrksrc="git-branchless")
    self.install_license("LICENSE-MIT")
    self.do(
        self.chroot_cwd
        / f"target/{self.profile().triplet}/release/git-branchless",
        "install-man-pages",
        self.chroot_destdir / "usr/share/man",
    )
