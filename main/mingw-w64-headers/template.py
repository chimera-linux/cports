pkgname = "mingw-w64-headers"
pkgver = "13.0.0"
pkgrel = 0
build_wrksrc = "mingw-w64-headers"
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool"]
depends = []
pkgdesc = "Header files for Windows development"
license = "ZPL-2.1"
url = "https://www.mingw-w64.org"
source = f"$(SOURCEFORGE_SITE)/mingw-w64/mingw-w64-v{pkgver}.tar.bz2"
sha256 = "5afe822af5c4edbf67daaf45eec61d538f49eef6b19524de64897c6b95828caf"
options = ["empty"]

_targets = ["x86_64", "i686", "aarch64", "armv7"]

for _an in _targets:
    depends += [self.with_pkgver(f"mingw-w64-headers-{_an}")]


def configure(self):
    from cbuild.util import gnu_configure

    for an in _targets:
        at = an + "-w64-mingw32"
        gnu_configure.configure(
            self,
            configure_args=[
                f"--host={at}",
                f"--prefix=/usr/{at}",
            ],
            build_dir=f"build-{an}",
        )


def build(self):
    for an in _targets:
        self.make.build(wrksrc=f"build-{an}")


def check(self):
    for an in _targets:
        self.make.check(wrksrc=f"build-{an}")


def install(self):
    for an in _targets:
        self.make.install(
            wrksrc=f"build-{an}",
        )


def _gen(an, at):
    @subpackage(f"mingw-w64-headers-{an}")
    def _(self):
        self.subdesc = f"{an} support"
        return [f"usr/{at}"]


for _an in _targets:
    _at = _an + "-w64-mingw32"
    _gen(_an, _at)
