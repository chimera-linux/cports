pkgname = "binfmt-support"
pkgver = "2.2.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libpipeline-devel"]
triggers = ["/usr/share/binfmts"]
pkgdesc = "Support for extra binary formats"
maintainer = "eater <=@eater.me>"
license = "GPL-3.0-or-later"
url = "https://gitlab.com/cjwatson/binfmt-support"
source = f"https://download.savannah.nongnu.org/releases/binfmt-support/binfmt-support-{pkgver}.tar.gz"
sha256 = "cce14163f9b526283e6f0d00f3be1cfe239fa2c7574e5e0ba8ad3db74166a4a5"


def post_install(self):
    # we don't need that
    self.rm(self.destdir / "etc", recursive=True)
    self.install_service(self.files_path / "binfmt-support")
