pkgname = "oksh"
pkgver = "7.9"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
make_dir = "."
makedepends = ["ncurses-devel"]
pkgdesc = "Portable OpenBSD ksh, based on pdksh"
license = "custom:none"
url = "https://github.com/ibara/oksh"
source = f"{url}/releases/download/oksh-{pkgver}/oksh-{pkgver}.tar.gz"
sha256 = "51b2d92515950c959dbf24f6fc33336db8c0526c2a50fee4ca598a18a6114a49"
hardening = ["vis", "cfi"]
# There are no tests
options = ["!check"]


def post_install(self):
    self.install_shell("/usr/bin/oksh")
