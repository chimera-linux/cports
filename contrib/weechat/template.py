pkgname = "weechat"
pkgver = "4.3.4"
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
    "zlib-ng-compat-devel",
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
sha256 = "f8695b25a99b8825f33798ac2f2a6a3e4c640361dc71e19a16ffc345d69df610"


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
