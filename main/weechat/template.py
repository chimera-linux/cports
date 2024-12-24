pkgname = "weechat"
pkgver = "4.5.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DENABLE_ENCHANT=ON",
    # no system v8 available (lol)
    "-DENABLE_JAVASCRIPT=OFF",
    # who uses this
    "-DENABLE_PHP=OFF",
    "-DENABLE_DOC=ON",
    "-DENABLE_DOC_INCOMPLETE=ON",
    "-DENABLE_MAN=ON",
    # missing dependency (cpputest); tests seem kinda half broken
    "-DENABLE_TESTS=OFF",
]
hostmakedepends = [
    "asciidoctor",
    "cmake",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "cjson-devel",
    "enchant-devel",  # spell plugin
    "gnutls-devel",
    "guile-devel",
    "curl-devel",
    "libgcrypt-devel",
    "lua5.4-devel",  # lua plugin
    "ncurses-devel",
    "perl",  # perl plugin
    "python-devel",  # python plugin
    "ruby-devel",  # ruby plugin
    "tcl-devel",  # tcl plugin
    "zlib-ng-compat-devel",  # relay plugin
    "zstd-devel",
]
pkgdesc = "Extensible chat client"
maintainer = "eater <=@eater.me>"
license = "GPL-3.0-or-later"
url = "https://weechat.org"
source = f"https://weechat.org/files/src/weechat-{pkgver}.tar.gz"
sha256 = "aae869ab8fe872961587ed487c2cad4627453118afa1510f536d53844785e1da"


@subpackage("weechat-devel")
def _(self):
    return self.default_devel()


def _plugin(name):
    @subpackage(f"weechat-{name}")
    def _(self):
        self.subdesc = f"{name.capitalize()} plugin"
        self.depends = [self.parent]

        return [f"usr/lib/weechat/plugins/{name}.so"]


for _p in [
    "guile",
    "lua",
    "perl",
    "python",
    "ruby",
    "tcl",
]:
    _plugin(_p)
