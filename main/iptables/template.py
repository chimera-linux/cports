pkgname = "iptables"
pkgver = "1.8.10"
pkgrel = 2
build_style = "gnu_configure"
configure_args = [
    "--enable-devel",
    "--enable-shared",
    "--enable-bpf-compiler",
]
hostmakedepends = ["automake", "flex", "libtool", "pkgconf"]
makedepends = [
    "flex-devel-static",
    "libpcap-devel",
    "libmnl-devel",
    "libnfnetlink-devel",
    "libnetfilter_conntrack-devel",
    "libnftnl-devel",
    "linux-headers",
]
depends = [
    "cmd:iptables!iptables-nft",
    "cmd:iptables-save!iptables-nft",
    "cmd:iptables-restore!iptables-nft",
    "cmd:ip6tables!iptables-nft",
    "cmd:ip6tables-save!iptables-nft",
    "cmd:ip6tables-restore!iptables-nft",
]
checkdepends = ["python", "bash"]
pkgdesc = "Linux packet filtering system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://www.netfilter.org/projects/iptables"
source = f"{url}/files/iptables-{pkgver}.tar.xz"
sha256 = "5cc255c189356e317d070755ce9371eb63a1b783c34498fb8c30264f3cc59c9c"


@subpackage("iptables-libs")
def _(self):
    # transitional
    self.provides = [
        self.with_pkgver("libiptc"),
        self.with_pkgver("libxtables"),
    ]

    return self.default_libs()


@subpackage("iptables-devel")
def _(self):
    # transitional
    self.provides = [
        self.with_pkgver("libiptc-devel"),
        self.with_pkgver("libxtables-devel"),
    ]

    return self.default_devel()


def post_install(self):
    fpath = self.files_path

    # service-related bits
    self.install_file(fpath / "iptables-flush", "usr/libexec", mode=0o755)
    self.install_file(fpath / "iptables-start", "usr/libexec", mode=0o755)
    self.install_service(self.files_path / "iptables")
    self.install_service(self.files_path / "ip6tables")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")

    # some default config files to be populated (originally from void)
    for f in ["empty", "simple_firewall"]:
        self.install_file(fpath / f"{f}.rules", "usr/share/xtables/etc")
    for f in ["filter", "mangle", "nat", "raw", "security"]:
        self.install_file(fpath / f"empty-{f}.rules", "usr/share/xtables/var")

    # make room for defaults
    for f in ["tables", "tables-save", "tables-restore"]:
        self.uninstall(f"usr/bin/ip{f}")
        self.uninstall(f"usr/bin/ip6{f}")


@subpackage("iptables-nft")
def _(self):
    self.subdesc = "use nftables"
    self.install_if = [self.parent]  # prefer

    return [
        "@usr/bin/iptables=>xtables-nft-multi",
        "@usr/bin/ip6tables=>xtables-nft-multi",
        "@usr/bin/iptables-save=>xtables-nft-multi",
        "@usr/bin/ip6tables-save=>xtables-nft-multi",
        "@usr/bin/iptables-restore=>xtables-nft-multi",
        "@usr/bin/ip6tables-restore=>xtables-nft-multi",
    ]


@subpackage("iptables-legacy")
def _(self):
    self.subdesc = "use legacy"

    return [
        "@usr/bin/iptables=>xtables-legacy-multi",
        "@usr/bin/ip6tables=>xtables-legacy-multi",
        "@usr/bin/iptables-save=>xtables-legacy-multi",
        "@usr/bin/ip6tables-save=>xtables-legacy-multi",
        "@usr/bin/iptables-restore=>xtables-legacy-multi",
        "@usr/bin/ip6tables-restore=>xtables-legacy-multi",
    ]
