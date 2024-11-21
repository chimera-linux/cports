pkgname = "mercurial"
pkgver = "6.9"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "gettext-devel",
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
sha256 = "629604293df2be8171ec856bf4f8b4faa8e4305af13607dce0f89f74132836d6"
# a lot of them fail just due to different positions of messages in a diff
options = ["!check"]


def check(self):
    self.do("python", "run-tests.py", wrksrc="tests")


def post_build(self):
    self.do("make", "-C", "doc", "man")
    self.do("make", "-C", "contrib/chg")


def post_install(self):
    self.do(
        "make",
        "-C",
        "doc",
        "install",
        f"DESTDIR={self.chroot_destdir}",
        "PREFIX=/usr",
    )
    self.do(
        "make",
        "-C",
        "contrib/chg",
        "install",
        f"DESTDIR={self.chroot_destdir}",
        "PREFIX=/usr",
    )
