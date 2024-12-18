pkgname = "chicken"
pkgver = "6.0.0_pre1"
pkgrel = 0
build_style = "configure"
configure_args = ["--prefix=/usr"]
depends = [self.with_pkgver("chicken-devel")]
pkgdesc = "Practical and portable Scheme system"
license = "BSD-3-Clause"
url = "https://call-cc.org"
source = (
    "https://code.call-cc.org/dev-snapshots/2024/12/09/chicken-6.0.0pre1.tar.gz"
)
sha256 = "a4beda4eede1e2aa81f1c7d6cd71e0d0f2d3b9aa0023209984f1810fa29e7629"
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
