pkgname = "ntpd-rs"
pkgver = "1.9.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["dinit-chimera"]
pkgdesc = "Full-featured implementation of NTP, including NTS support"
license = "Apache-2.0 OR MIT"
url = "https://trifectatech.org/projects/ntpd-rs"
source = f"https://github.com/pendulum-project/{pkgname}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b25d560c4ae5a704d9509984b040123675052d27fe7a3e7cbc5bedc9e392c932"


def check(self):
    # Reported here:
    # https://github.com/pendulum-project/ntpd-rs/issues/2286
    self.cargo.check(
        args=[
            "--",
            "--skip",
            "daemon::spawn::nts::tests::allow_srv_direct_name_resolution",
            "--skip",
            "daemon::ntp_source::tests::test_deny_stops_poll",
            "--skip",
            "daemon::ntp_source::tests::test_timeroundtrip",
        ]
    )


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/ntp-daemon")
    self.install_bin(f"target/{self.profile().triplet}/release/ntp-ctl")

    self.install_sysusers("^/sysusers.conf")
    self.install_tmpfiles("^/tmpfiles.conf")
    self.install_service("^/ntp-daemon")

    self.install_file(
        "docs/examples/conf/ntp.toml.default",
        "etc/ntpd-rs",
        name="ntp.toml",
    )

    self.install_man("docs/precompiled/man/ntp-ctl.8")
    self.install_man("docs/precompiled/man/ntp-daemon.8")
    self.install_man("docs/precompiled/man/ntp.toml.5")

    self.install_license("LICENSE-APACHE")
    self.install_license("LICENSE-MIT")
