pkgname = "mercurial"
pkgver = "7.0.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "gettext-devel",
    "python-build",
    "python-docutils",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
makedepends = ["python-devel"]
depends = ["python"]
checkdepends = ["python-pytest", "unzip"]
pkgdesc = "Distributed source control management"
license = "GPL-2.0-or-later"
url = "https://www.mercurial-scm.org"
source = f"https://www.mercurial-scm.org/release/mercurial-{pkgver}.tar.gz"
sha256 = "f7731f1b42acaeaacb8cf7e41c0a472a7aa31a8f47e518baea735f1cb2987e0c"
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
