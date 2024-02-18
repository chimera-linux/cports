pkgname = "mpg123"
pkgver = "1.32.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-optimization=0",
    "--with-default-audio=pulse",
    "--enable-ipv6=yes",
    "--enable-network=yes",
    "--disable-lfs-alias",
]
hostmakedepends = [
    "automake",
    "libltdl-devel",
    "libtool",
    "pkgconf",
]
makedepends = [
    "libpulse-devel",
    "linux-headers",
    "pipewire-jack-devel",
    "sdl-devel",
]
depends = [f"mpg123-output-dummy={pkgver}-r{pkgrel}"]
pkgdesc = "MPEG 1.0/2.0/2.5 audio player"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://www.mpg123.org"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "af908cdf6cdb6544b97bc706a799f79894e69468af5881bf454a0ebb9171ed63"


def _genlib(libn, descn, iif):
    @subpackage(f"mpg123-output-{libn}")
    def _out(self):
        self.pkgdesc = f"{pkgdesc} ({descn} output plugin)"
        if iif:
            self.install_if = [f"{pkgname}-libs={pkgver}-r{pkgrel}", iif]

        return [f"usr/lib/mpg123/output_{libn}.so"]


for _libn, _descn, _iif in [
    ("oss", "OSS", None),
    ("jack", "JACK", "jack"),
    ("pulse", "PulseAudio", "libpulse"),
    ("sdl", "SDL", "sdl"),
    ("dummy", "dummy", None),
]:
    _genlib(_libn, _descn, _iif)


@subpackage("mpg123-libs")
def _libs(self):
    self.depends = [f"mpg123-output-dummy={pkgver}-r{pkgrel}"]

    return self.default_libs()


@subpackage("mpg123-devel")
def _devel(self):
    return self.default_devel()
