pkgname = "mingw-w64-zlib-ng-compat"
pkgver = "2.3.3"
# compat version
_cver = "1.3.1"
pkgrel = 0
build_style = "configure"
hostmakedepends = []
pkgdesc = "Zlib compression library for Windows development"
license = "Zlib"
url = "https://github.com/zlib-ng/zlib-ng"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f9c65aa9c852eb8255b636fd9f07ce1c406f061ec19a2e7d508b318ca0c907d1"
# TODO: tests in Wine
options = ["empty", "!check"]

_targets = ["x86_64", "i686", "aarch64", "armv7"]

for _an in _targets:
    hostmakedepends += [
        f"clang-mingw-w64-{_an}",
    ]


def pre_configure(self):
    for an in _targets:
        self.mkdir(f"build-{an}")


def configure(self):
    for an in _targets:

        at = an + "-w64-mingw32"
        _c_args = [
            f"--prefix=/usr/{at}",
            f"--libdir=/usr/{at}/lib",
            f"--sharedlibdir=/usr/{at}/lib",
            f"--includedir=/usr/{at}/include",
            "--shared",
            "--zlib-compat",
        ]
        # TODO: make a proper patch: fails to compile some inline asm 
        if an == "armv7":
            _c_args += ["--without-optimizations"]
        self.do(
            self.chroot_cwd / self.configure_script,
            *_c_args,
            wrksrc=f"build-{an}",
            env={
                "CC": f"{at}-clang",
                "CHOST": at,
                "CFLAGS": "-fPIC",
                "LDFLAGS": "",
            },
        )


def build(self):
    for an in _targets:
        at = an + "-w64-mingw32"
        # configure overrides these to {at}-windres, {at}-strip, so we reassign it
        self.do(
            "make",
            f"RC=llvm-windres --target={at} -I /usr/{at}/include",
            "STRIP=llvm-strip",
            wrksrc=f"build-{an}",
        )


def check(self):
    for an in _targets:
        self.make.check(wrksrc=f"build-{an}")


def post_install(self):
    for an in _targets:
        at = an + "-w64-mingw32"
        # Probably better for binary compatibility with Windows applications?
        # see: https://lists.pagure.io/archives/list/mingw@lists.fedoraproject.org/thread/7IB4DLFPAFRKJKXXGJPUITI4WCI4N7RX/?sort=thread
        # and: https://src.fedoraproject.org/rpms/mingw-zlib/blob/rawhide/f/mingw-zlib-cmake.patch
        self.rename(
            f"usr/{at}/bin/libz-1.dll",
            f"usr/{at}/bin/zlib1.dll",
            relative=False,
        )


def install(self):
    for an in _targets:
        self.make.install(wrksrc=f"build-{an}")


def _gen(an, at):
    @subpackage(f"mingw-w64-zlib-ng-compat-{an}")
    def _(self):
        self.subdesc = f"{an} support"
        self.options = ["linkundefver"]  # is it needed?
        return [f"usr/{at}"]


for _an in _targets:
    _at = _an + "-w64-mingw32"
    _gen(_an, _at)
