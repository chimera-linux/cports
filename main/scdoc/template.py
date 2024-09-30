pkgname = "scdoc"
pkgver = "1.11.3"
pkgrel = 0
build_style = "makefile"
make_build_args = []
make_install_args = []
make_check_args = []
hostmakedepends = ["pkgconf"]
pkgdesc = "Tool for generating roff manual pages"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://git.sr.ht/~sircmpwn/scdoc"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "4c5c6136540384e5455b250f768e7ca11b03fdba1a8efc2341ee0f1111e57612"
patch_style = "patch"
hardening = ["vis", "cfi"]

if self.profile().cross:
    hostmakedepends += ["scdoc"]
    make_build_args += ["HOST_SCDOC=/usr/bin/scdoc"]
    make_check_args += ["HOST_SCDOC=/usr/bin/scdoc"]
    make_install_args += ["HOST_SCDOC=/usr/bin/scdoc"]


def post_install(self):
    self.install_license("COPYING")
