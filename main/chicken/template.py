pkgname = "chicken"
pkgver = "6.0.0"
pkgrel = 0
build_style = "configure"
configure_args = ["--prefix=/usr"]
depends = [self.with_pkgver("chicken-devel")]
pkgdesc = "Practical and portable Scheme system"
license = "BSD-3-Clause"
url = "https://call-cc.org"
source = f"https://code.call-cc.org/releases/{pkgver}/chicken-{pkgver}.tar.gz"
sha256 = "92835552b1b687ad26737e429b5aba36510bf429f8816ec0f6d336c8cb41f443"
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
