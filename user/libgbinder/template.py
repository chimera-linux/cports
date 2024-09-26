pkgname = "libgbinder"
pkgver = "1.1.40"
pkgrel = 1
build_style = "makefile"
make_install_target = "install-dev"
make_check_target = "test"
make_use_env = True
hostmakedepends = ["bison", "flex", "pkgconf"]
makedepends = ["libglibutil-devel", "linux-headers"]
pkgdesc = "GLib-style interface to binder"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "BSD-3-Clause"
url = "https://github.com/mer-hybris/libgbinder"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "9e86243df6502ffd0a68ee8384c5c36b9cd4093733ea620313f1947f312abbd1"


def post_build(self):
    self.make.invoke(["-C", "test"])


def post_install(self):
    self.make.invoke(
        ["-C", "test", f"DESTDIR={self.chroot_destdir}", "install"]
    )
    self.install_license("LICENSE")


@subpackage("libgbinder-progs")
def _(self):
    return self.default_progs()


@subpackage("libgbinder-devel")
def _(self):
    return self.default_devel()
