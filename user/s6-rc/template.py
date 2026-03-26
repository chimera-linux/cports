pkgname = "s6-rc"
pkgver = "0.6.0.0"
pkgrel = 0
build_style = "makefile"
makedepends = [
  "skalibs-devel",
  "execline-devel"
  "s6-devel"
]
depends = [
  "skalibs",
  "execline",
  "s6"
]
options = [
  "!check",
  "!cross"
]
hardening = [
  "cfi",
  "sst"
]
pkgdesc = "Simple service manager based on s6"
license = "ISC"
url = "https://skarnet.org/software/s6-rc"
source = f"https://skarnet.org/software/s6-rc/s6-rc-{pkgver}.tar.gz"
sha256 = "46d4a62959ef16097b84dcfb0c3b31a6ff49aa476d4aeec9c5b7bde1ce684901"

@subpackage("s6-rc-repo")
def _(self):
  self.subdesc = "service tree management"
  self.depends = [
    "skalibs",
    "execline"
  ]
  self.install_if = ["s6-rc"]
  return ["usr/bin/s6-rc-repo-*", "usr/bin/s6-rc-set-*"]
