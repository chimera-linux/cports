pkgname = "git-absorb"
pkgver = "0.6.13"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "pkgconf", "asciidoc"]
makedepends = ["libgit2-devel"]
pkgdesc = "Automatic git commit --fixup; like hg absorb"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "BSD-3-Clause"
url = "https://github.com/tummychow/git-absorb"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "5646857dd764d0a486405e777b3ec4e919511abc96bd0e02e71ec9e94d151115"


def post_build(self):
    self.do("make", "-C", "Documentation")


def post_install(self):
    self.install_license("LICENSE.md")
    self.install_man("Documentation/git-absorb.1")
