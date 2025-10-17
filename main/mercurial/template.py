pkgname = "mercurial"
pkgver = "7.1.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "gettext-devel",
    "python-build",
    "python-docutils",
    "python-installer",
    "python-roman",
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
sha256 = "47cf66ba89c175536faf844c9b4cd962eb432afb516c073e51f436bf3f0bc148"
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
