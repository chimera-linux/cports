pkgname = "66-tools"
pkgver = "0.1.2.0"
pkgrel = 0
build_style = "meson"
configure_args = [
  "-Denable-all-pic=true",
  "-Denable-pie=true",
  "-Dwith-doc=true",
#  "-Denable-dbus=elogind"
]
makedepends = [
  "skalibs-devel",
  "execline-devel"
  "s6-devel",
  "oblibs-devel",
  "linux-headers",
#  "elogind-devel"
  "lowdown"
]
depends = ["oblibs"]
options = [
  "!check",
  "!cross"
]
hardening = [
  "cfi",
  "sst"
]
install_if = ["66-init"]
pkgdesc = "Extra tools and helpers with 66"
license = "ISC"
url = "https://web.obarun.org/software/66-tools/{pkgver}/index"
source = f"https://git.obarun.org/Obarun/66-tools/-/archive/{pkgver}/66-tools-{pkgver}.tar.gz"

# This subpackage is disabled for the time being
# until some other problems and issues are sorted out
#@subpackage("66-dbus-launch")
#def _(self):
#  self.subdesc = "dbus-broker controller and dbus-activation through 66"
#  self.depends = [
#    "oblibs",
#    "elogind-libs"
#  ]
#  self.install_if = [
#    "dbus-broker",
#    "66-init"
#  ]
#  return ["usr/bin/66-dbus-launch"]

@subpackage("66-ns")
def _(self):
  self.subdesc = "namespacing and sandboxing processes"
  self.depends = ["oblibs"]
  self.install_if = [
    "66-init",
    "66-tools"
  ]
  return ["usr/bin/66-ns"]

@subpackage("66-ns-rules")
def _(self):
  self.subdesc = "ns rules"
  self.depends = ["oblibs"]
  self.install_if = ["66-ns"]
  return ["usr/share/66/script/ns"]

@subpackage("66-tools-execl")
def _(self):
  self.subdesc = "convenience helpers for execline"
  self.depends = ["oblibs"]
  self.install_if = ["execline"]
  return ["usr/bin/execl-*"]
