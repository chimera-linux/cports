pkgname = "mingw-w64-crt"
pkgver = "11.0.1"
pkgrel = 0
build_wrksrc = "mingw-w64-crt"
build_style = "gnu_configure"
configure_args = ["--disable-dependency-tracking"]
make_cmd = "gmake"
hostmakedepends = ["autoconf", "automake", "libtool", "gmake"]
depends = []
pkgdesc = "Complete runtime environment for Windows (runtime)"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "ZPL-2.1"
url = "https://www.mingw-w64.org"
source = f"$(SOURCEFORGE_SITE)/mingw-w64/mingw-w64-v{pkgver}.tar.bz2"
sha256 = "3f66bce069ee8bed7439a1a13da7cb91a5e67ea6170f21317ac7f5794625ee10"
# checks fail
options = ["empty", "!check"]

_targets = ["x86_64", "i686", "aarch64", "armv7"]

for _an in _targets:
    hostmakedepends += [f"mingw-w64-headers-{_an}"]
    depends += [f"mingw-w64-crt-{_an}={pkgver}-r{pkgrel}"]


def do_configure(self):
    for an in _targets:
        at = an + "-w64-mingw32"
        eargs = [
            f"--host={at}",
            f"--prefix=/usr/{at}",
        ]
        match an:
            case "x86_64":
                eargs += ["--disable-lib32"]
            case "i686":
                eargs += ["--disable-lib64"]
            case "aarch64" | "armv7":
                eargs += ["--disable-lib32", "--disable-lib64"]
        self.mkdir(f"build-{an}")
        with self.stamp(f"{an}_configure") as s:
            s.check()
            self.do(
                self.chroot_cwd / "configure",
                *configure_args,
                *eargs,
                wrksrc=f"build-{an}",
                env={
                    "CC": f"clang -target {at}",
                    "CFLAGS": "",
                    "LDFLAGS": "",
                },
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
    @subpackage(f"mingw-w64-crt-{an}")
    def _subp(self):
        return [f"usr/{at}"]


for _an in _targets:
    _at = _an + "-w64-mingw32"
    _gen(_an, _at)
