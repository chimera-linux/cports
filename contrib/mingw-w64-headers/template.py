pkgname = "mingw-w64-headers"
pkgver = "12.0.0"
pkgrel = 0
build_wrksrc = "mingw-w64-headers"
build_style = "gnu_configure"
hostmakedepends = ["autoconf", "automake", "libtool"]
depends = []
pkgdesc = "Header files for Windows development"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "ZPL-2.1"
url = "https://www.mingw-w64.org"
source = f"$(SOURCEFORGE_SITE)/mingw-w64/mingw-w64-v{pkgver}.tar.bz2"
sha256 = "cc41898aac4b6e8dd5cffd7331b9d9515b912df4420a3a612b5ea2955bbeed2f"
options = ["empty"]

_targets = ["x86_64", "i686", "aarch64", "armv7"]

for _an in _targets:
    depends += [self.with_pkgver(f"mingw-w64-headers-{_an}")]


def do_configure(self):
    from cbuild.util import gnu_configure

    for an in _targets:
        at = an + "-w64-mingw32"
        with self.stamp(f"{an}_configure") as s:
            s.check()
            gnu_configure.configure(
                self,
                configure_args=[
                    f"--host={at}",
                    f"--prefix=/usr/{at}",
                ],
                build_dir=f"build-{an}",
            )


def do_build(self):
    for an in _targets:
        with self.stamp(f"{an}_build") as s:
            s.check()
            self.make.build(wrksrc=f"build-{an}")


def do_check(self):
    for an in _targets:
        with self.stamp(f"{an}_check") as s:
            s.check()
            self.make.check(wrksrc=f"build-{an}")


def do_install(self):
    for an in _targets:
        with self.stamp(f"{an}_install") as s:
            s.check()
            self.make.install(
                wrksrc=f"build-{an}",
            )


def _gen(an, at):
    @subpackage(f"mingw-w64-headers-{an}")
    def _subp(self):
        self.subdesc = f"{an} support"
        return [f"usr/{at}"]


for _an in _targets:
    _at = _an + "-w64-mingw32"
    _gen(_an, _at)
