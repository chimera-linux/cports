pkgname = "mingw-w64-headers"
pkgver = "11.0.1"
pkgrel = 0
build_wrksrc = "mingw-w64-headers"
build_style = "gnu_configure"
hostmakedepends = ["autoconf", "automake", "libtool"]
depends = []
pkgdesc = "Header files for Windows"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "ZPL-2.1"
url = "https://www.mingw-w64.org"
source = f"$(SOURCEFORGE_SITE)/mingw-w64/mingw-w64-v{pkgver}.tar.bz2"
sha256 = "3f66bce069ee8bed7439a1a13da7cb91a5e67ea6170f21317ac7f5794625ee10"
options = ["empty"]

_targets = ["x86_64", "i686", "aarch64", "armv7"]

for _an in _targets:
    depends += [f"mingw-w64-headers-{_an}={pkgver}-r{pkgrel}"]


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
        self.pkgdesc = f"{pkgdesc} ({an} support)"
        return [f"usr/{at}"]


for _an in _targets:
    _at = _an + "-w64-mingw32"
    _gen(_an, _at)
