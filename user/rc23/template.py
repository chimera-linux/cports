pkgname = "rc23"
pkgver = "2.0.6"
pkgrel = 0
build_style = "makefile"
make_build_args = ["RC_ADDON=1", "EDIT=edit"]
makedepends = ["libedit-readline-devel"]
pkgdesc = "Reimplementation of the Plan 9 rc shell"
license = "Zlib"
url = "https://codeberg.org/rc23/rc23"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "badb52822f578a0ae4b9fadf32d65acfad9a312798bb1c3a8bc5c9e02da5158e"


def post_install(self):
    self.install_shell("/usr/bin/rc23")
