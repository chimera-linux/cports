pkgname = "pam_wrapper"
pkgver = "1.1.5"
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
sha256 = "bbc47d9990eef7b33db55d63a9e2cde5d16e8989a17c6456b8ca2a582d72f889"


@subpackage("pam_wrapper-devel")
def _devel(self):
    return self.default_devel()
