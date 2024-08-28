pkgname = "mingw-w64-winpthreads"
pkgver = "12.0.0"
pkgrel = 1
build_wrksrc = "mingw-w64-libraries/winpthreads"
build_style = "gnu_configure"
configure_args = ["--disable-dependency-tracking"]
hostmakedepends = ["automake", "libtool"]
depends = []
checkdepends = []
pkgdesc = "POSIX threading APIs for Windows development"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "ZPL-2.1"
url = "https://www.mingw-w64.org"
source = f"$(SOURCEFORGE_SITE)/mingw-w64/mingw-w64-v{pkgver}.tar.bz2"
sha256 = "cc41898aac4b6e8dd5cffd7331b9d9515b912df4420a3a612b5ea2955bbeed2f"
# check requires libunwind
options = ["empty", "!check", "!lto"]

_targets = ["x86_64", "i686", "aarch64", "armv7"]

for _an in _targets:
    hostmakedepends += [f"mingw-w64-headers-{_an}"]
    checkdepends += [f"mingw-w64-crt-{_an}"]


def configure(self):
    for an in _targets:
        at = an + "-w64-mingw32"
        eargs = [
            f"--host={at}",
            f"--prefix=/usr/{at}",
        ]
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


def build(self):
    for an in _targets:
        self.make.build(wrksrc=f"build-{an}")


def check(self):
    for an in _targets:
        self.make.check(wrksrc=f"build-{an}")


def install(self):
    for an in _targets:
        at = an + "-w64-mingw32"
        self.make.install(wrksrc=f"build-{an}")

        # don't step on mingw-w64-headers
        for hdr in ["signal", "time", "unistd"]:
            self.uninstall(f"usr/{at}/include/pthread_{hdr}.h")


def _gen(an, at):
    @subpackage(f"mingw-w64-winpthreads-{an}")
    def _(self):
        self.subdesc = an
        self.depends = [f"mingw-w64-crt-{an}"]
        # coff
        self.options = ["!strip"]

        return [f"usr/{at}"]

    depends.append(self.with_pkgver(f"mingw-w64-winpthreads-{_an}"))


for _an in _targets:
    _at = _an + "-w64-mingw32"
    _gen(_an, _at)
