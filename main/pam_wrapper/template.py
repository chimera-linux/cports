pkgname = "pam_wrapper"
pkgver = "1.1.7"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DUNIT_TESTING=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf", "python-setuptools"]
makedepends = ["linux-pam-devel", "python-devel"]
checkdepends = ["cmocka-devel"]
pkgdesc = "Tool to test PAM applications and modules"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-3.0-or-later"
url = "https://cwrap.org/pam_wrapper.html"
source = f"https://ftp.samba.org/pub/cwrap/pam_wrapper-{pkgver}.tar.gz"
sha256 = "d1c93e2b687d08834df0e09026dd63d2ce4f577701d406a013e9a8afe469bde1"
patch_style = "patch"


@subpackage("pam_wrapper-python")
def _(self):
    self.subdesc = "Python bindings"
    self.depends += ["python"]

    return ["usr/lib/python*"]


@subpackage("pam_wrapper-devel")
def _(self):
    return self.default_devel()
