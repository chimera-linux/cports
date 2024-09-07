pkgname = "incus"
pkgver = "6.5.0"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/..."]
make_check_args = ["-skip", "TestConvertNetworkConfig", "./..."]
hostmakedepends = [
    "go",
    "pkgconf",
]
makedepends = [
    "acl-devel",
    "cowsql-devel",
    "libatomic-chimera-devel-static",
    "libseccomp-devel",
    "libcap-devel",
    "linux-headers",
    "libuv-devel",
    "libunwind-devel-static",
    "lxc-devel",
    "musl-devel-static",
    "raft-devel",
    "sqlite-devel",
    "udev-devel",
]
depends = [
    "acl-progs",
    "attr-progs",
    "dnsmasq",
    "iptables",
    "libvirt",
    "lxc",
    "rsync",
    "squashfs-tools",
    "util-linux",
    "xz",
    self.with_pkgver("incus-client"),
]
go_build_tags = ["libsqlite3"]
go_check_tags = ["libsqlite3"]
pkgdesc = "Powerful system container and virtual machine manager"
maintainer = "tj <tjheeta@gmail.com>"
license = "Apache-2.0"
url = "https://github.com/lxc/incus"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "aabc762bdcfe210b777e6b78e40150c9ffbc798aa39c8b4ba55812dac3ada0ec"
# fail to link because of post_build overrides
options = ["!check"]


def post_build(self):
    # Build the agent statically
    self.env["CGO_ENABLED"] = "1"
    self.env["CGO_LDFLAGS"] = "-static-pie"
    self.go_build_tags = ["agent", "netgo", "osusergo"]
    self.make_build_args = ["./cmd/incus-agent"]
    self.golang.build()


def post_install(self):
    self.install_service(self.files_path / "incus")
    self.install_service(self.files_path / "incus-user")
    self.install_sysusers(self.files_path / "sysusers.conf")


@subpackage("incus-client")
def _(self):
    self.subdesc = "client only"
    self.depends = [self.parent]

    return ["usr/bin/incus"]
