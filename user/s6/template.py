pkgname = "s6"
pkgver = "2.14.0.1"
pkgrel = 0
build_style = "makefile"
makedepends = ["skalibs-devel"]
depends = [
  "skalibs",
  "s6-accessrules"
]
options = [
  "!check",
  "!cross"
]
hardening = [
  "cfi",
  "sst"
]
pkgdesc = "s6 suite by skarnet"
subdesc = "process supervision"
license = "ISC"
url = "https://skarnet.org/software/s6"
source = f"http://skarnet.org/software/s6/s6-{pkgver}.tar.gz"
sha256 = "c25afe817cbc3f594efc5050351f8b9101ba78616d0ce915658f370e7ee2e258"

@subpackage("s6-ftrig")
def _(self):
  self.subdesc = "notification"
  self.depends = ["skalibs"]
  self.install_if = ["s6"]
  self.url = "http://skarnet.org/software/s6/ftrig.html#notification"
  return ["usr/bin/s6-*fifodir", "usr/bin/s6-ftrig*"]

@subpackage("s6-log")
def _(self):
  self.subdesc = "logging"
  self.depends = ["skalibs"]
  self.install_if = ["s6"]
  return ["usr/bin/s6-log", "usr/bin/s6-socklog", "usr/bin/ucspilogd"]

@subpackage("s6-instance")
def _(self):
  self.subdesc = "instantiation for s6"
  self.depends = ["s6"]
  self.url = "http://skarnet.org/software/s6/instances.html"
  return ["usr/bin/s6-instance-*"]

@subpackage("s6-accessrules")
def _(self):
  self.subdesc = "accessrules interface; conversion b/w cdb and plaintext"
  self.depends = ["skalibs"]
  return ["usr/bin/s6-accessrules-*"]

@subpackage("s6-fdholder")
def _(self):
  self.subdesc = "fd-holding tools"
  self.depends = ["s6-accessrules"]
  return ["usr/bin/s6-fdholder*"]

@subpackage("s6-ipc")
def _(self):
  self.subdesc = "ipc socket helpers including an inetd replacement"
  self.depends = ["s6-accessrules"]
  return ["usr/bin/s6-ipcclient", "usr/bin/s6-ipcserver*", "usr/bin/s6-ioconnect", "usr/bin/s6-connlimit"]

@subpackage("s6-sudo")
def _(self):
  self.subdesc = "suidless alternative using ipc server"
  self.url = "http://skarnet.org/software/s6/s6-sudo.html"
  self.depends = ["s6-ipc"]
  return ["usr/bin/s6-sudo*"]
