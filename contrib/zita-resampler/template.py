pkgname = "zita-resampler"
pkgver = "1.11.2"
pkgrel = 0
build_style = "makefile"
make_dir = "source"
make_use_env = True
pkgdesc = "Library for resampling audio signals"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-3.0-or-later"
url = "https://kokkinizita.linuxaudio.org/linuxaudio"
source = f"{url}/downloads/zita-resampler-{pkgver}.tar.xz"
sha256 = "aa5c54e696069af26f3f1fed4a963113cc1237cddfd57ae5842abcb1acd5492c"
# no tests
options = ["!check"]


@subpackage("zita-resampler-devel")
def _(self):
    return self.default_devel()
