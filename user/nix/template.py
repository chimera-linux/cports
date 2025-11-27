pkgname = "nix"
pkgver = "2.28.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",
    "--localstatedir=/nix/var/",
    "-Dbindings=false",
    "-Ddefault_library=shared",
    "-Ddoc-gen=true",  # man pages.
    # We don't do test as it requires network, so don't build them.
    "-Dunit-tests=false",
]
hostmakedepends = [
    "bash",
    "bison",
    "cmake",
    "doxygen",
    "flex",
    "jq",
    "mdbook",
    "meson",
    "pkgconf",
    "rsync",
]
makedepends = [
    "blake3-devel",
    "boost-devel",
    "brotli-devel",
    "curl-devel",
    "editline-devel",
    "gc-devel",
    "libarchive-devel",
    "libgit2-devel",
    "libseccomp-devel",
    "libsodium-devel",
    "lowdown-devel",
    "nlohmann-json",
    "openssl3-devel",
    "sqlite-devel",
    "toml11",
]
pkgdesc = "Purely functional package manager"
license = "LGPL-2.1-or-later"
url = "https://github.com/NixOS/nix"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "5081f335d5d4754e0a34f47ea76b3826faa1108f464aa5b7f6c4d43034b07bc1"
# int causes segfault
hardening = ["!int"]
# checks require network
options = ["!check", "!cross"]


def post_install(self):
    self.uninstall("usr/lib/systemd")
    self.uninstall("usr/lib/tmpfiles.d")

    self.install_sysusers(
        self.files_path / "nix-daemon.sysusers.conf", name="nix-daemon"
    )
    self.install_sysusers(self.files_path / "nix.sysusers.conf", name="nix")
    self.install_service(
        self.files_path / "nix-daemon.dinit", name="nix-daemon"
    )
    self.install_file(self.files_path / "nix.conf", "etc/nix")
    self.install_file(
        self.files_path / "nix.defaults", "etc/default", name="nix"
    )

    # upstream scripts clutter up $PATH in nested shells and assume location of nix profile
    # without checking nix.conf
    self.uninstall("usr/etc/profile.d")
    self.install_file(
        self.files_path / "nix.profile.d", "usr/lib/profile.d", name="nix.sh"
    )

    # html docs
    self.uninstall("usr/share/doc/nix/")


@subpackage("nix-devel")
def _(self):
    return self.default_devel()
