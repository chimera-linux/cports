pkgname = "sdl1.2_ttf"
pkgver = "2.0.11"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
hostmakedepends = ["automake", "pkgconf"]
makedepends = [
    "freetype-devel",
    "sdl12-compat-devel",
]
pkgdesc = "TrueType support for SDL legacy branch"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Zlib"
url = "https://www.libsdl.org/projects/old/SDL_ttf/release-1.2.html"
source = (
    f"https://www.libsdl.org/projects/SDL_ttf/release/SDL_ttf-{pkgver}.tar.gz"
)
sha256 = "724cd895ecf4da319a3ef164892b72078bd92632a5d812111261cde248ebcdb7"


@subpackage("sdl1.2_ttf-devel")
def _(self):
    return self.default_devel()
