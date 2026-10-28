pkgname = "zabbix-agent"
pkgver = "7.0.32"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--sysconfdir=/usr/lib/zabbix-agent",
    "--enable-agent",
    "--enable-ipv6",
    "--with-libcurl",
    "--with-libpcre2",
    "--with-openssl",
]
make_dir = "."
hostmakedepends = ["automake", "pkgconf"]
makedepends = [
    "curl-devel",
    "dinit-chimera",
    "libevent-devel",
    "linux-headers",
    "openssl3-devel",
    "pcre2-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Zabbix monitoring agent"
license = "AGPL-3.0-only"
url = "https://www.zabbix.com"
source = f"https://cdn.zabbix.com/zabbix/sources/stable/{pkgver[:3]}/zabbix-{pkgver}.tar.gz"
sha256 = "ead5b0723ad965eb0e79f98d5d2b89088e7c898ae194eeba767e5d1fb2d50a96"
tool_flags = {
    "CFLAGS": ["-D_LARGEFILE64_SOURCE"],
    # needed for loadable modules
    "LDFLAGS": ["-Wl,--export-dynamic"],
}
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "zabbix-agentd")

    # defaults live in /usr/lib, local overrides are read from /etc/zabbix;
    # the last assignment wins so the include must come after everything else
    conf = self.destdir / "usr/lib/zabbix-agent/zabbix_agentd.conf"
    conf.write_text(
        conf.read_text()
        .replace(
            "# PidFile=/tmp/zabbix_agentd.pid",
            "PidFile=/run/zabbix/zabbix_agentd.pid",
        )
        .replace(
            "LogFile=/tmp/zabbix_agentd.log",
            "LogFile=/var/log/zabbix/zabbix_agentd.log",
        )
        + "\n### Local overrides\nInclude=/etc/zabbix/zabbix_agentd.d/*.conf\n"
    )
