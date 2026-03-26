pkgname = "s6-linux-init"
pkgver = "1.2.0.0"
pkgrel = 0
build_style = "makefile"
makedepends = [
  "skalibs-devel",
  "execline-devel"
  "s6-devel"
]
depends = [
  "s6",
  "execline"
]
options = [
  "!check",
  "!cross"
]
hardening = [
  "cfi",
  "sst"
]
install_if = ["s6-rc"]
pkgdesc = "Boot-time stage1 PID-1 for s6-rc"
license = "ISC"
url = "https://skarnet.org/software/s6-linux-init"
source = f"https://skarnet.org/software/s6-linux-init/s6-linux-init-{pkgver}.tar.gz"
