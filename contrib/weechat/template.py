pkgname = "weechat"
pkgver = "4.2.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    # no guile available
    "-DENABLE_GUILE=False",
    # no php available
    "-DENABLE_PHP=False",
    # no v8 available
    "-DENABLE_JAVASCRIPT=False",
    # no, aspell available
    "-DENABLE_ENCHANT=True",
    # missing dependencies
    "-DENABLE_TESTS=False",
    "-DENABLE_MAN=False",
    "-DENABLE_DOC=False",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "gettext"]
makedepends = [
    # core deps
    "libgcrypt-devel",
    "gnutls-devel",
    "zstd-devel",
    "libcurl-devel",
    "ncurses-devel",
    # perl plugin
    "perl",
    # lua plugin
    "lua5.4-devel",
    # pyhton plugin
    "python-devel",
    # relay plugin
    "zlib-devel",
    # ruby plugin
    "ruby-devel",
    # spell plugin
    "enchant-devel",
    # tcl plugin
    "tcl-devel",
]
pkgdesc = "Extensible chat client"
maintainer = "eater <=@eater.me>"
license = "GPL-3.0-or-later"
url = "https://weechat.org"
source = f"https://weechat.org/files/src/weechat-{pkgver}.tar.gz"
sha256 = "064856ae2b999ab13e5eb6c40d15333d3afe428d636ed3849f2d48a825379706"


@subpackage("weechat-devel")
def _devel(self):
    return self.default_devel()


def _plugin(name):
    @subpackage(f"weechat-{name}")
    def _plg(self):
        self.pkgdesc = f"{pkgdesc} ({name.capitalize()} plugin)"
        self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]

        return [f"usr/lib/weechat/plugins/{name}.so"]


for _p in ["lua", "python", "ruby", "tcl", "perl"]:
    _plugin(_p)
