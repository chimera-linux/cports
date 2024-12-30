pkgname = "fftw"
pkgver = "3.3.10"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = []
pkgdesc = "Library for computing the discrete Fourier transform"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://www.fftw.org"
source = f"{url}/fftw-{pkgver}.tar.gz"
sha256 = "56c932549852cddcfafdab3820b0200c7742675be92179e59e6215b340e26467"
# flaky
options = ["!check"]


match self.profile().arch:
    case "aarch64" | "ppc64le" | "ppc64" | "riscv64" | "x86_64":
        makedepends += ["libomp-devel"]
        _have_omp = True
    case _:
        _have_omp = False


def pre_configure(self):
    self.do("autoreconf", "-if")


def configure(self):
    from cbuild.util import gnu_configure

    gnu_configure.replace_guess(self)

    eargs = ["--enable-shared", "--enable-threads"]
    sseargs = []
    sse2args = []
    if _have_omp:
        eargs += ["--enable-openmp"]
    match self.profile().arch:
        case "x86_64":
            sseargs += ["--enable-sse"]
            sse2args += ["--enable-sse2"]

    gnu_configure.configure(
        self, build_dir="build-double", extra_args=eargs + sse2args
    )
    gnu_configure.configure(
        self,
        build_dir="build-long-double",
        extra_args=[*eargs, "--enable-long-double"],
    )
    gnu_configure.configure(
        self,
        build_dir="build-float",
        extra_args=[*eargs, "--enable-float", *sseargs],
    )


def build(self):
    for f in ["double", "long-double", "float"]:
        self.make.build(wrksrc=f"build-{f}")


def install(self):
    for f in ["double", "long-double", "float"]:
        self.make.install(wrksrc=f"build-{f}")


def check(self):
    for f in ["double", "long-double", "float"]:
        self.make.check(wrksrc=f"build-{f}")


@subpackage("fftw-libs")
def _(self):
    return self.default_libs()


@subpackage("fftw-devel")
def _(self):
    return self.default_devel(extra=["usr/share/info"])
