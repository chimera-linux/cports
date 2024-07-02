pkgname = "flite"
pkgver = "2.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-shared", "--with-audio=pulseaudio"]
make_cmd = "gmake"
# not full autotools, just configure
make_dir = "."
make_build_args = ["-j1"]
make_check_target = ""
make_check_args = ["-C", "testsuite", "do_thread_test"]
hostmakedepends = [
    "automake",
    "gmake",
]
makedepends = [
    "alsa-lib-devel",
    "libomp-devel",
    "libpulse-devel",
    "linux-headers",
]
pkgdesc = "Speech synthesis engine"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-4-Clause"
url = "http://cmuflite.org"
source = f"https://github.com/festvox/flite/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ab1555fe5adc3f99f1d4a1a0eb1596d329fd6d74f1464a0097c81f53c0cf9e5c"
# tools/ uses #define const to strip const away from includes to build which
# also breaks fortify
tool_flags = {"CFLAGS": ["-U_FORTIFY_SOURCE"]}


def init_check(self):
    self.env["LD_LIBRARY_PATH"] = str(
        f"{self.chroot_builddir}/{pkgname}-{pkgver}/build/{self.profile().arch}-linux-musl/lib"
    )


def post_install(self):
    self.install_license("COPYING")


@subpackage("flite-devel")
def _devel(self):
    return self.default_devel()
