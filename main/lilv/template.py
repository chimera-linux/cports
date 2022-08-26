pkgname = "lilv"
pkgver = "0.24.18"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "libsndfile-devel", "python-devel", "serd-devel", "sord-devel",
    "sratom-devel", "lv2"
]
pkgdesc = "C API for using LV2 plugins"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "https://drobilla.net/software/lilv.html"
source = f"https://download.drobilla.net/{pkgname}-{pkgver}.tar.xz"
sha256 = "f65814ae60be54d65f1671dff7538aeddcda3610cb6e46ec96de47f84ab0f3b8"

def post_install(self):
    self.install_license("COPYING")
    self.install_dir("usr/share/bash-completion/completions")
    self.mv(
        self.destdir / "etc/bash_completion.d/lilv",
        self.destdir / "usr/share/bash-completion/completions"
    )

@subpackage("lilv-devel")
def _devel(self):
    return self.default_devel()

@subpackage("lilv-progs")
def _progs(self):
    return self.default_progs()
