pkgname = "s6-portable-utils"
pkgver = "2.3.1.1"
pkgrel = 0
build_style = "makefile"
makedepends = ["skalibs-devel"]
depends = [
  "skalibs",
  "s6-ln"
]
options = [
  "!check",
  "!cross"
]
hardening = [
  "cfi",
  "sst"
]
pkgdesc = "s6 miscellaneous portable UNIX utilities"
license = "ISC"
url = "https://skarnet.org/software/s6-portable-utils"
source = f"https://skarnet.org/software/s6-portable-utils/s6-portable-utils-{pkgver}.tar.gz"
sha256 = "cf08d71963c0ea1708cdd82bd40ad301154bccc59b68eefb428aa79b42273242"

@subpackage("s6-ln")
def _(self):
  self.subdesc = "ln which supports atomic force-linking"
  # It's separate because sometimes it's the only tool needed
  self.depends = ["skalibs"]
  return ["usr/bin/s6-ln"]
