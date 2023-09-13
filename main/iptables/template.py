pkgname = "iptables"
pkgver = "1.8.9"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--enable-devel",
    "--enable-shared",
    "--enable-bpf-compiler",
]
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake", "flex"]
makedepends = [
    "libfl-devel-static",
    "libpcap-devel",
    "libmnl-devel",
    "libnfnetlink-devel",
    "libnetfilter_conntrack-devel",
    "libnftnl-devel",
    "linux-headers",
]
depends = [
    "virtual:cmd:iptables!iptables-nft",
    "virtual:cmd:iptables-save!iptables-nft",
    "virtual:cmd:iptables-restore!iptables-nft",
    "virtual:cmd:ip6tables!iptables-nft",
    "virtual:cmd:ip6tables-save!iptables-nft",
    "virtual:cmd:ip6tables-restore!iptables-nft",
]
checkdepends = ["python", "bash"]
pkgdesc = "Linux packet filtering system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://www.netfilter.org/projects/iptables"
source = f"{url}/files/{pkgname}-{pkgver}.tar.xz"
sha256 = "ef6639a43be8325a4f8ea68123ffac236cb696e8c78501b64e8106afb008c87f"


@subpackage("libiptc")
def _iptc(self):
    self.pkgdesc = "Netfilter libiptc library"
    return ["usr/lib/libip[46]tc.so.*"]


@subpackage("libiptc-devel")
def _iptc_devel(self):
    self.pkgdesc = "Netfilter libiptc library (development files)"
    return [
        "usr/include/libiptc",
        "usr/lib/libip[46]tc.so",
        "usr/lib/pkgconfig/libiptc.pc",
        "usr/lib/pkgconfig/libip[46]tc.pc",
    ]


@subpackage("libxtables")
def _xtables(self):
    self.pkgdesc = "Netfilter xtables library"
    return ["usr/lib/libxtables.so.*"]


@subpackage("libxtables-devel")
def _xtables_devel(self):
    self.pkgdesc = "Netfilter xtables library (development files)"
    return [
        "usr/include/xtables*.h",
        "usr/lib/libxtables.so",
        "usr/lib/pkgconfig/xtables.pc",
    ]


def post_install(self):
    fpath = self.files_path

    # service-related bits
    self.install_file(fpath / "iptables-flush", "usr/libexec", mode=0o755)
    self.install_file(fpath / "iptables-start", "usr/libexec", mode=0o755)
    self.install_service(self.files_path / "iptables")
    self.install_service(self.files_path / "ip6tables")

    # config files/rules taken from void
    for f in ["empty", "simple_firewall"]:
        self.install_file(fpath / f"{f}.rules", "etc/iptables")
    for f in ["filter", "mangle", "nat", "raw", "security"]:
        self.install_file(fpath / f"empty-{f}.rules", "var/lib/iptables")

    # make room for defaults
    for f in ["tables", "tables-save", "tables-restore"]:
        self.rm(self.destdir / f"usr/bin/ip{f}", force=True)
        self.rm(self.destdir / f"usr/bin/ip6{f}", force=True)


@subpackage("iptables-nft")
def _nft(self):
    self.pkgdesc = f"{pkgdesc} (use nftables)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]  # prefer

    def inst():
        self.mkdir(self.destdir / "usr/bin", parents=True)
        for f in ["tables", "tables-save", "tables-restore"]:
            self.ln_s("xtables-nft-multi", self.destdir / f"usr/bin/ip{f}")
            self.ln_s("xtables-nft-multi", self.destdir / f"usr/bin/ip6{f}")

    return inst


@subpackage("iptables-legacy")
def _legacy(self):
    self.pkgdesc = f"{pkgdesc} (use legacy)"

    def inst():
        self.mkdir(self.destdir / "usr/bin", parents=True)
        for f in ["tables", "tables-save", "tables-restore"]:
            self.ln_s("xtables-legacy-multi", self.destdir / f"usr/bin/ip{f}")
            self.ln_s("xtables-legacy-multi", self.destdir / f"usr/bin/ip6{f}")

    return inst


configure_gen = []
