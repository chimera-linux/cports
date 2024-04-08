pkgname = "mercurial"
pkgver = "6.7.4"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "gettext-devel",
    "gmake",
    "python-build",
    "python-docutils",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["python-devel"]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Distributed source control management"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-2.0-or-later"
url = "https://www.mercurial-scm.org"
source = f"https://www.mercurial-scm.org/release/mercurial-{pkgver}.tar.gz"
sha256 = "74708f873405c12272fec116c6dd52862e8ed11c10011c7e575f5ea81263ea5e"
# vendored dependencies tests are broken on python 3.11 and up
options = ["!check"]


def post_build(self):
    self.do("gmake", "man", wrksrc="doc")


def post_install(self):
    self.do(
        "gmake",
        "install",
        f"DESTDIR={self.chroot_destdir}",
        "PREFIX=/usr",
        wrksrc="doc",
    )
    self.install_completion("contrib/bash_completion", "bash")
    self.install_completion("contrib/zsh_completion", "zsh")
