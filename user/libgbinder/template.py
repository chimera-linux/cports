pkgname = "libgbinder"
pkgver = "1.1.43"
pkgrel = 0
build_style = "makefile"
make_install_target = "install-dev"
make_check_target = "test"
make_use_env = True
hostmakedepends = ["bison", "flex", "pkgconf"]
makedepends = ["libglibutil-devel", "linux-headers"]
pkgdesc = "GLib-style interface to binder"
license = "BSD-3-Clause"
url = "https://github.com/mer-hybris/libgbinder"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "31e40d30b5624352681a0eb4e155708679b0349e084913e419f5b3c2c668ac76"


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
