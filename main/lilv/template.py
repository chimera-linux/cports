pkgname = "lilv"
pkgver = "0.24.22"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "libsndfile-devel",
    "python-devel",
    "serd-devel",
    "sord-devel",
    "sratom-devel",
    "lv2",
]
pkgdesc = "C API for using LV2 plugins"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "https://drobilla.net/software/lilv.html"
source = f"https://download.drobilla.net/{pkgname}-{pkgver}.tar.xz"
sha256 = "76f949d0e59fc83363409b5ec5e15c1046fb7dd6589d3c1b920cec1fd29f9ff3"
# FIXME cfi
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")
    self.install_dir("usr/share/bash-completion/completions")
    self.mv(
        self.destdir / "etc/bash_completion.d/lilv",
        self.destdir / "usr/share/bash-completion/completions",
    )


@subpackage("lilv-devel")
def _devel(self):
    return self.default_devel()


@subpackage("lilv-progs")
def _progs(self):
    return self.default_progs()
