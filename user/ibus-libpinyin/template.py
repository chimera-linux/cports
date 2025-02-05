pkgname = "ibus-libpinyin"
pkgver = "1.15.8"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--enable-cloud-input-mode",
    "--enable-opencc",
    "--enable-boost",
]
hostmakedepends = ["intltool", "libtool", "pkgconf", "automake", "gsed"]
makedepends = [
    "gettext-devel",
    "sqlite-devel",
    "opencc-devel",
    "lua5.4-devel",
    "ibus-devel",
    "libpinyin-devel",
    "libsoup-devel",
    "json-glib-devel",
    "boost-devel",
    "python-gobject-devel",
    "util-linux-uuid-devel",
]
depends = ["ibus"]
pkgdesc = "Intelligent Pinyin engine based on libpinyin for IBus"
maintainer = "metalparade <comer@live.cn>"
license = "GPL-3.0-or-later"
url = "https://github.com/libpinyin/ibus-libpinyin"
source = f"{url}/releases/download/{pkgver}/ibus-libpinyin-{pkgver}.tar.gz"
sha256 = "1d32eb82a09bc043da0e2b65849bc61c8820b99f30a8cff10d807a1c44848bfa"
exec_wrappers = [("/usr/bin/gsed", "sed")]
