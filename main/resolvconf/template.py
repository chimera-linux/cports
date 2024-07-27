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
    self.subdesc = "use symlink"
    self.install_if = [self.parent, "cmd:resolvconf"]
    self.depends = [
        self.parent,
        "virtual:cmd:resolvconf!resolvconf",
    ]
    return ["usr/lib/tmpfiles.d"]


@subpackage("resolvconf-openresolv")
def _openresolv(self):
    self.subdesc = "openresolv"
    self.install_if = [self.parent]  # prefer
    self.provides = [self.with_pkgver("resolvconf-any")]
    self.depends = ["openresolv"]
    self.options = ["brokenlinks"]

    return [
        "@usr/bin/resolvconf=>resolvconf-openresolv",
        "@usr/share/man/man8/resolvconf.8=>resolvconf-openresolv.8",
    ]


@subpackage("resolvconf-none")
def _none(self):
    self.subdesc = "do not use"
    self.provides = [self.with_pkgver("resolvconf-any")]
    return []
