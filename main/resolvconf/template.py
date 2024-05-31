pkgname = "resolvconf"
pkgver = "1.0"
pkgrel = 1
build_style = "meta"
pkgdesc = "Metapackage for resolv.conf management"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"


def post_install(self):
    # tmpfiles.d
    self.install_tmpfiles(self.files_path / "resolv.conf", name="resolv")


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

    return [
        "@usr/bin/resolvconf=>resolvconf-openresolv",
        "@usr/share/man/man8/resolvconf.8=>resolvconf-openresolv.8",
    ]


@subpackage("resolvconf-none")
def _none(self):
    self.pkgdesc = f"{pkgdesc} (do not use)"
    self.provides = [f"resolvconf-any={pkgver}-r{pkgrel}"]
    return []
