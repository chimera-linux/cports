pkgname = "fail2ban"
pkgver = "1.1.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
makedepends = ["dinit-chimera"]
depends = ["python-pyasynchat"]
pkgdesc = "Daemon to ban hosts that cause multiple auth errors"
license = "GPL-2.0-only"
url = "https://fail2ban.org"
source = f"https://github.com/fail2ban/fail2ban/archive/{pkgver}.tar.gz"
sha256 = "474fcc25afdaf929c74329d1e4d24420caabeea1ef2e041a267ce19269570bae"
# doesn't work with pytest
options = ["!check"]


def post_install(self):
    self.uninstall("usr/lib/python*/site-packages/fail2ban/tests", glob=True)
    # asyncore+asynchat
    self.uninstall("usr/lib/python*/site-packages/fail2ban/compat", glob=True)
    # pep517 can't install to normal paths
    with self.pushd(self.destdir / "usr/lib/python*/site-packages", glob=True):
        self.mv("usr/share", self.destdir / "usr")
        self.mv("etc", self.destdir)
    # service last
    self.install_service(self.files_path / "fail2ban")
