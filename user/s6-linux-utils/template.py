pkgname = "s6-linux-utils"
pkgver = "2.6.4.0"
pkgrel = 0
build_style = "makefile"
makedepends = ["skalibs-devel"]
depends = ["skalibs"]
options = [
  "!check",
  "!cross"
]
hardening = [
  "cfi",
  "sst"
]
pkgdesc = "s6 miscellaneous linux utilities"
license = "ISC"
url = "https://skarnet.org/software/s6-linux-utils"
source = f"https://skarnet.org/software/s6-linux-utils/s6-linux-utils-{pkgver}.tar.gz"
sha256 = "cc727f70d5e8780433a497acb7cb3100656b3126589ab02e9d2042006c794cf2"

@subpackage("s6-rc-fstab")
def _(self):
  self.subdesc = "generates s6-rc service definitions from fstab"
  self.depends = ["skalibs"]
  self.install_if = ["s6-rc"]
  return ["ust/bin/fstab2s6c"]

@subpackage("s6-rngseed")
def _(self):
  self.subdesc = "random seed management"
  self.depends = ["skalibs"]
  return ["usr/bin/rngseed"]
