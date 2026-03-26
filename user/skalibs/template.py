pkgname = "skalibs"
pkgver = "2.14.5.1"
pkgrel = 0
build_style = "makefile"
options = [
  "!check",
  "!cross"
]
hardening = [
  "cfi",
  "sst"
]
pkgdesc = "General-purpose low-level C lib by skarnet"
license = "ISC"
url = "https://skarnet.org/software/skalibs/"
source = f"https://git.skarnet.org/cgi-bin/cgit.cgi/skalibs/about/skalibs-{pkgver}.tar.gz"
sha256 = "fa359c70439b480400a0a2ef68026a2736b315025a9d95df69d34601fb938f0f"
