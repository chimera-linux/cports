pkgname = "aubio"
pkgver = "0.4.9"
pkgrel = 2
build_style = "waf"
hostmakedepends = [
    "doxygen",
    "pkgconf",
    "python-sphinx",
    "txt2man",
]
makedepends = [
    "ffmpeg-devel",
    "libsamplerate-devel",
    "libsndfile-devel",
    "pipewire-jack-devel",
]
pkgdesc = "Library for audio and music analysis"
license = "GPL-3.0-or-later"
url = "https://aubio.org"
# bundled waf uses deprecated python modules
_waf_ver = "2.0.25"
source = [
    f"{url}/pub/aubio-{pkgver}.tar.bz2",
    f"!https://waf.io/waf-{_waf_ver}",
]
sha256 = [
    "d48282ae4dab83b3dc94c16cf011bcb63835c1c02b515490e1883049c3d1f3da",
    "21199cd220ccf60434133e1fd2ab8c8e5217c3799199c82722543970dc8e38d5",
]
# tests run in build phase
options = ["!check"]


def post_extract(self):
    # replace bundled waf
    self.rm("waf")
    self.rm("waflib", recursive=True)
    self.mv(self.sources_path / f"waf-{_waf_ver}", "waf")


@subpackage("aubio-progs")
def _(self):
    return self.default_progs()


@subpackage("aubio-devel")
def _(self):
    return self.default_devel()
