pkgname = "weechat"
pkgver = "4.0.3"
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
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    # core deps
    "libgcrypt-devel",
    "gnutls-devel",
    "libzstd-devel",
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
sha256 = "e9ef6a2e843c852440ed793d83b25f97c18e8655d18aed9b343577683cf1b6f1"


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
