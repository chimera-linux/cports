pkgname = "ladspa-sdk"
pkgver = "1.17"
pkgrel = 1
makedepends = ["libsndfile-devel"]
pkgdesc = "Linux Audio Developer's Simple Plugin API"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "http://www.ladspa.org"
source = f"{url}/download/ladspa_sdk_{pkgver}.tgz"
sha256 = "27d24f279e4b81bd17ecbdcc38e4c42991bb388826c0b200067ce0eb59d3da5b"


def build(self):
    self.do("make", "-C", "src")
    self.rm("doc/ladspa.h.txt", force=True)


def check(self):
    self.do("make", "-C", "src", "test")


def install(self):
    # header
    self.install_file("src/ladspa.h", "usr/include")
    # plugins
    for f in (self.cwd / "plugins").glob("*.so*"):
        self.install_file(f, "usr/lib/ladspa", mode=0o755)
    # programs
    self.install_files("bin", "usr/bin")
    # docs
    self.install_dir("usr/share/doc")
    self.cp("doc", self.destdir / "usr/share/doc/ladspa-sdk", recursive=True)
    self.install_link(
        "usr/share/doc/ladspa-sdk/ladspa.h.txt", "../../../include/ladspa.h"
    )


@subpackage("ladspa-sdk-plugins")
def _(self):
    self.subdesc = "example plugins"

    return ["usr/lib/ladspa"]


@subpackage("ladspa-sdk-progs")
def _(self):
    return self.default_progs()
