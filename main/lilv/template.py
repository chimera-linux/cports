pkgname = "lilv"
pkgver = "0.24.26"
pkgrel = 1
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "libsndfile-devel",
    "lv2",
    "python-devel",
    "serd-devel",
    "sord-devel",
    "sratom-devel",
]
pkgdesc = "C API for using LV2 plugins"
license = "ISC"
url = "https://drobilla.net/software/lilv.html"
source = f"https://download.drobilla.net/lilv-{pkgver}.tar.xz"
sha256 = "22feed30bc0f952384a25c2f6f4b04e6d43836408798ed65a8a934c055d5d8ac"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")
    self.rename(
        "etc/bash_completion.d/lilv",
        "usr/share/bash-completion/completions/lv2info",
        relative=False,
    )


@subpackage("lilv-devel")
def _(self):
    return self.default_devel()


@subpackage("lilv-progs")
def _(self):
    return self.default_progs()
