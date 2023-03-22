pkgname = "weechat"
pkgver = "3.8"
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
    "libgcrypt-devel", "gnutls-devel", "libzstd-devel", "libcurl-devel", "ncurses-devel",
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
license = "GPL-3.0"
url = "https://weechat.org"
source = f"https://weechat.org/files/src/weechat-{pkgver}.tar.gz"
sha256 = "d9d27fac127c724564cf28c6179fa6ecc79a61f9dad09a3b251500f2b0755409"


@subpackage("weechat-devel")
def _devel(self):
    return self.default_devel()


@subpackage("weechat-lua")
def _lua(self):
    return ["usr/lib/weechat/plugins/lua.so"]


@subpackage("weechat-python")
def _python(self):
    return ["usr/lib/weechat/plugins/python.so"]


@subpackage("weechat-ruby")
def _ruby(self):
    return ["usr/lib/weechat/plugins/ruby.so"]


@subpackage("weechat-tcl")
def _tcl(self):
    return ["usr/lib/weechat/plugins/tcl.so"]


@subpackage("weechat-perl")
def _tcl(self):
    return ["usr/lib/weechat/plugins/perl.so"]
