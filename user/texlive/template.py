pkgname = "texlive"
pkgver = "20240312"
pkgrel = 0
build_wrksrc = "build"
build_style = "configure"
configure_script = "../configure"
configure_args = [
    "-C",
    "--prefix=/usr",
    "--sysconfdir=/etc",
    "--disable-native-texlive-build",
    "--disable-silent-rules",
    "--disable-static",
    "--disable-xdvik",  # XXX: Needs libXaw
    "--enable-shared",
    "--enable-tex-synctex",
    "--with-banner-add=/Chimera Linux",
    "--with-system-cairo",
    "--with-system-freetype2",
    "--with-system-gd",
    "--with-system-gmp",
    "--with-system-graphite2",
    "--with-system-harfbuzz",
    "--with-system-icu",
    "--with-system-libpaper",
    "--with-system-libpng",
    "--with-system-mpfr",
    "--with-system-pixman",
    "--with-system-potrace",
    "--with-system-teckit",
    "--with-system-zlib",
    "--with-system-zziplib",
    # "--with-system-kpathsea",
    # "--with-system-ptexenc",
]
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "freetype-devel",
    "gmp-devel",
    "graphite2-devel",
    "harfbuzz-devel",
    "icu-devel",
    "libgd-devel",
    "libpaper-devel",
    "libpng-devel",
    "mpfr-devel",
    "pixman-devel",
    "potrace-devel",
    "teckit-devel",
    "zlib-ng-compat-devel",
    "zziplib-devel",
]
depends = [self.with_pkgver("texmf")]
pkgdesc = "Comprehensive TeX distribution"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "GPL-3.0-or-later"
url = "https://tug.org/texlive"
source = f"https://ftp.math.utah.edu/pub/tex/historic/systems/texlive/{pkgver[:4]}/texlive-{pkgver}-source.tar.xz"
sha256 = "7b6d87cf01661670fac45c93126bed97b9843139ed510f975d047ea938b6fe96"
broken_symlinks = ["usr/bin/*"]
# XXX: few tests are failing with SIGILL
options = ["!check"]


def post_extract(self):
    self.mkdir(self.build_wrksrc)
    for lib in (
        "cairo",
        "freetype2",
        "gd",
        "gmp",
        "graphite2",
        "harfbuzz",
        "icu",
        "libpaper",
        "libpng",
        "mpfr",
        "pixman",
        "potrace",
        "teckit",
        "zlib",
        "zziplib",
    ):
        self.rm(f"libs/{lib}", recursive=True)


def post_install(self):
    # texmf-dist is provided by texmf
    self.uninstall("usr/share/texmf-dist")


@subpackage("texlive-libs")
def _(self):
    return self.default_libs()


@subpackage("texlive-devel")
def _(self):
    return self.default_devel()
