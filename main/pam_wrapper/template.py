pkgname = "pam_wrapper"
pkgver = "1.1.8"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DUNIT_TESTING=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf", "python-setuptools"]
makedepends = ["linux-pam-devel", "python-devel"]
checkdepends = ["cmocka-devel"]
pkgdesc = "Tool to test PAM applications and modules"
license = "GPL-3.0-or-later"
url = "https://cwrap.org/pam_wrapper.html"
source = f"https://ftp.samba.org/pub/cwrap/pam_wrapper-{pkgver}.tar.gz"
sha256 = "6549c0b3e41d1ebe0c94a1be63c25eec918191462b602ab6f47d4a5fa709c3e4"


def post_extract(self):
    # lol
    self.rm(".git", recursive=True)


@subpackage("pam_wrapper-python")
def _(self):
    self.subdesc = "Python bindings"
    self.depends += ["python"]

    return ["usr/lib/python*"]


@subpackage("pam_wrapper-devel")
def _(self):
    return self.default_devel()
