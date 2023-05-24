pkgname = "resolvconf"
pkgver = "1.0"
pkgrel = 0
build_style = "meta"
pkgdesc = "Metapackage for resolv.conf management"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"


def post_install(self):
    # tmpfiles.d
    self.install_file(self.files_path / "resolv.conf", "usr/lib/tmpfiles.d")


@subpackage("resolvconf-symlink")
def _symlink(self):
    self.pkgdesc = f"{pkgdesc} (use symlink)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "cmd:resolvconf"]
    self.depends = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "virtual:cmd:resolvconf!resolvconf",
    ]
    return ["usr/lib/tmpfiles.d"]


@subpackage("resolvconf-openresolv")
def _openresolv(self):
    self.pkgdesc = f"{pkgdesc} (openresolv)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]  # prefer
    self.provides = [f"resolvconf-any={pkgver}-r{pkgrel}"]
    self.depends = ["openresolv"]
    self.options = ["brokenlinks"]

    def inst():
        self.mkdir(self.destdir / "usr/bin", parents=True)
        self.mkdir(self.destdir / "usr/share/man/man8", parents=True)
        self.ln_s("resolvconf-openresolv", self.destdir / "usr/bin/resolvconf")
        self.ln_s(
            "resolvconf-openresolv.8",
            self.destdir / "usr/share/man/man8/resolvconf.8",
        )

    return inst


@subpackage("resolvconf-none")
def _none(self):
    self.pkgdesc = f"{pkgdesc} (do not use)"
    self.provides = [f"resolvconf-any={pkgver}-r{pkgrel}"]
    return []
