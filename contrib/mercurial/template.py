pkgname = "mercurial"
pkgver = "6.8.1"
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
checkdepends = ["python-pytest", "unzip"]
pkgdesc = "Distributed source control management"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-2.0-or-later"
url = "https://www.mercurial-scm.org"
source = f"https://www.mercurial-scm.org/release/mercurial-{pkgver}.tar.gz"
sha256 = "030e8a7a6d590e4eaeb403ee25675615cd80d236f3ab8a0b56dcc84181158b05"
# a lot of them fail just due to different positions of messages in a diff
options = ["!check"]


def do_check(self):
    self.do("python", "run-tests.py", wrksrc="tests")


def post_build(self):
    self.do("gmake", "-C", "doc", "man")
    self.do("gmake", "-C", "contrib/chg")


def post_install(self):
    self.do(
        "gmake",
        "-C",
        "doc",
        "install",
        f"DESTDIR={self.chroot_destdir}",
        "PREFIX=/usr",
    )
    self.do(
        "gmake",
        "-C",
        "contrib/chg",
        "install",
        f"DESTDIR={self.chroot_destdir}",
        "PREFIX=/usr",
    )
