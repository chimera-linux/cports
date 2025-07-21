pkgname = "mpg123"
pkgver = "1.33.0"
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
    "libtool",
    "libtool-devel",
    "pkgconf",
]
makedepends = [
    "libpulse-devel",
    "linux-headers",
    "pipewire-jack-devel",
    "sdl2-compat-devel",
]
depends = [self.with_pkgver("mpg123-output-dummy")]
pkgdesc = "MPEG 1.0/2.0/2.5 audio player"
license = "LGPL-2.1-only"
url = "https://www.mpg123.org"
source = f"$(SOURCEFORGE_SITE)/mpg123/mpg123-{pkgver}.tar.bz2"
sha256 = "2290e3aede6f4d163e1a17452165af33caad4b5f0948f99429cfa2d8385faa9d"


def _genlib(libn, descn, iif):
    @subpackage(f"mpg123-output-{libn}")
    def _(self):
        self.subdesc = f"{descn} output plugin"
        if iif:
            self.install_if = [self.with_pkgver(f"{pkgname}-libs"), iif]

        return [f"usr/lib/mpg123/output_{libn}.so"]


for _libn, _descn, _iif in [
    ("oss", "OSS", None),
    ("jack", "JACK", "jack"),
    ("pulse", "PulseAudio", "libpulse"),
    ("sdl", "SDL", "sdl2"),
    ("dummy", "dummy", None),
]:
    _genlib(_libn, _descn, _iif)


@subpackage("mpg123-libs")
def _(self):
    self.depends = [self.with_pkgver("mpg123-output-dummy")]

    return self.default_libs()


@subpackage("mpg123-devel")
def _(self):
    return self.default_devel()
