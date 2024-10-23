pkgname = "roc-toolkit"
pkgver = "0.4.0"
pkgrel = 0
hostmakedepends = [
    "gengetopt",
    "pkgconf",
    "ragel",
    "scons",
]
makedepends = [
    "json-c-devel",
    "libatomic_ops-devel",
    "libltdl-devel",
    "libpulse-devel",
    "libsndfile-devel",
    "libunwind-devel",
    "libuv-devel",
    "openssl-devel",
    "speexdsp-devel",
]
pkgdesc = "Real-time audio streaming over the network"
maintainer = "triallax <triallax@tutanota.com>"
license = "MPL-2.0"
url = "https://roc-streaming.org"
source = f"https://github.com/roc-streaming/roc-toolkit/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "60501dfdc8c0de385898dbd1eb8239d93ef962667ddb064ad796b887a41a1a46"
hardening = ["vis", "cfi"]
# check: needs cpputest
# cross: scons, can't be bothered
options = ["!check", "!cross"]


_scons_flags = [
    "--disable-openfec",
    "--disable-sox",
    "--disable-alsa",
]


def build(self):
    self.do("scons", f"-j{self.make_jobs}", *_scons_flags)


def install(self):
    self.do(
        "scons", *_scons_flags, "install", env={"DESTDIR": self.chroot_destdir}
    )


@subpackage("roc-toolkit-devel")
def _(self):
    return self.default_devel()
