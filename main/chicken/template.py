pkgname = "chicken"
pkgver = "6.1.0"
pkgrel = 0
build_style = "configure"
configure_args = ["--prefix=/usr"]
depends = [self.with_pkgver("chicken-devel")]
pkgdesc = "Practical and portable Scheme system"
license = "BSD-3-Clause"
url = "https://call-cc.org"
source = f"https://code.call-cc.org/releases/{pkgver}/chicken-{pkgver}.tar.gz"
sha256 = "c6aee9a5374102ba318e0cfae62ded5e1825346577137952d7fb15b3094d49d8"
# is fwrapv so it mostly does not matter, still breaks tests on loongarch
hardening = ["!int"]


def init_build(self):
    self.make_env = {
        "LINKER_OPTIONS": self.get_ldflags(shell=True),
    }


def post_install(self):
    self.install_license("LICENSE")
    self.rename(
        "usr/share/chicken/doc", "usr/share/doc/chicken", relative=False
    )


@subpackage("chicken-devel")
def _(self):
    return self.default_devel()


@subpackage("chicken-libs")
def _(self):
    return self.default_libs(extra=["usr/lib/chicken"])
