pkgname = "conmon"
pkgver = "2.1.13"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
]
hostmakedepends = [
    "go-md2man",
    "meson",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "libseccomp-devel",
    "linux-headers",
]
pkgdesc = "OCI container monitor"
license = "Apache-2.0"
url = "https://github.com/containers/conmon"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "350992cb2fe4a69c0caddcade67be20462b21b4078dae00750e8da1774926d60"


def post_build(self):
    self.do("go-md2man", "-in", "docs/conmon.8.md", "-out", "docs/conmon.8")


def post_install(self):
    # the default containers-common config paths that podman and friends use
    # check /usr/libexec/podman hardcoded, but also /usr/bin is in the path.
    # so just link it, i guess... maybe this should be fixed by adding /usr/lib/
    # podman somehow to that path, as for all the other non-conmon stuff it does
    self.install_dir("usr/bin")
    self.install_link("usr/bin/conmon", "../lib/podman/conmon")
    self.install_man("docs/conmon.8")
