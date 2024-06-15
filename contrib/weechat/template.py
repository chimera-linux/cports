pkgname = "weechat"
pkgver = "4.3.2"
pkgrel = 1
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
    # missing dependency (cpputest); tests seem kinda half broken
    "-DENABLE_TESTS=False",
    "-DENABLE_MAN=True",
    "-DENABLE_DOC=True",
    "-DENABLE_DOC_INCOMPLETE=True",
]
hostmakedepends = [
    "asciidoctor",
    "cmake",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    # core deps
    "cjson-devel",
    "gnutls-devel",
    "libcurl-devel",
    "libgcrypt-devel",
    "ncurses-devel",
    "zstd-devel",
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
sha256 = "f3311a523d4b19c1ebed15dab7a2913bd0edabf69be345fe2095ff4e64506537"


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
