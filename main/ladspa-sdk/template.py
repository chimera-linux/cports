pkgname = "ladspa-sdk"
pkgver = "1.17"
pkgrel = 0
hostmakedepends = ["gmake"]
makedepends = ["libsndfile-devel"]
pkgdesc = "Linux Audio Developer's Simple Plugin API (LADSPA)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "http://www.ladspa.org"
source = f"{url}/download/ladspa_sdk_{pkgver}.tgz"
sha256 = "27d24f279e4b81bd17ecbdcc38e4c42991bb388826c0b200067ce0eb59d3da5b"


def do_build(self):
    self.do("gmake", "-C", "src")
    self.rm("doc/ladspa.h.txt", force=True)


def do_check(self):
    self.do("gmake", "-C", "src", "test")


def do_install(self):
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
        "/usr/include/ladspa.h", "usr/share/doc/ladspa-sdk/ladspa.h.txt"
    )


@subpackage("ladspa-sdk-plugins")
def _plugins(self):
    self.pkgdesc = f"{pkgdesc} (example plugins)"

    return ["usr/lib/ladspa"]


@subpackage("ladspa-sdk-progs")
def _progs(self):
    return self.default_progs()
