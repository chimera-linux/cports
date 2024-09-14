pkgname = "catfish"
pkgver = "4.18.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "intltool",
    "python-build",
    "python-distutils-extra",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "gtk+3",
    "python-cairo",
    "python-dbus",
    "python-gobject",
    "python-pexpect",
    "cmd:locate!chimerautils-extra",
    "xfconf",
]
pkgdesc = "Xfce file search tool"
maintainer = "triallax <triallax@tutanota.com>"
# TODO: https://gitlab.xfce.org/apps/catfish/-/issues/106
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/apps/catfish/start"
source = f"$(XFCE_SITE)/apps/catfish/{pkgver[:-2]}/catfish-{pkgver}.tar.bz2"
sha256 = "fdae9b73cc754a50716bb04b958aa31dbd7e94047068b7207f2ae313a7d58b99"
# No tests
options = ["!check"]
