pkgname = "kanidm"
pkgver = "1.6.4"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--package",
    "daemon",
    "--package",
    "kanidm-ipa-sync",
    "--package",
    "kanidm_tools",
    "--package",
    "kanidm_unix_int",
    "--package",
    "nss_kanidm",
    "--package",
    "pam_kanidm",
]
make_build_env = {"KANIDM_BUILD_PROFILE": "release_chimera"}
make_check_args = [*make_build_args]
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "linux-pam-devel",
    "openssl3-devel",
    "rust-std",
    "sqlite-devel",
    "udev-devel",
]
pkgdesc = "Modern and simple identity management platform written in rust"
license = "MPL-2.0"
url = "https://kanidm.com"
source = f"https://github.com/kanidm/kanidm/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4165a2762d5f5f6db5da34f084788f720d8f225dcbe35e00b650cefb6283bbd3"
options = ["empty"]


def post_prepare(self):
    self.cp(
        self.files_path / "release_chimera.toml",
        "libs/profiles",
    )


def install(self):
    # install binaries
    for executable in (
        "kanidm",
        "kanidmd",
        "kanidm-unix",
        "kanidm_unixd",
        "kanidm_unixd_tasks",
        "kanidm_ssh_authorizedkeys",
        "kanidm_ssh_authorizedkeys_direct",
    ):
        self.install_file(
            f"target/{self.profile().triplet}/release/{executable}",
            "usr/bin",
            mode=0o755,
        )

    # install libraries
    self.install_file(
        f"target/{self.profile().triplet}/release/libnss_kanidm.so",
        "usr/lib",
        name="libnss_kanidm.so.2",
    )
    self.install_file(
        f"target/{self.profile().triplet}/release/libpam_kanidm.so",
        "usr/lib/security",
        name="pam_kanidm.so",
    )

    # install configs
    self.install_file("examples/config", "etc/kanidm")
    self.install_file("examples/server.toml", "etc/kanidm")
    self.install_file("examples/unixd", "etc/kanidm")

    # install static files
    self.install_files("server/core/static", "usr/share/kanidm/ui", name="hpkg")

    # sysusers
    self.install_sysusers(
        self.files_path / "kanidmd-sysusers.conf", name="kanidmd"
    )
    self.install_sysusers(
        self.files_path / "kanidm-unixd-sysusers.conf", name="kanidm-unixd"
    )

    # tmpfiles
    self.install_tmpfiles(
        self.files_path / "kanidmd-tmpfiles.conf", name="kanidmd"
    )
    self.install_tmpfiles(
        self.files_path / "kanidm-unixd-tmpfiles.conf", name="kanidm-unixd"
    )

    # services
    self.install_service(self.files_path / "kanidmd")
    self.install_service(self.files_path / "kanidm-unixd")
    self.install_service(self.files_path / "kanidm-unixd-tasks")


@subpackage("kanidm-client")
def _(self):
    self.subdesc = "kanidm cli client"
    return ["usr/bin/kanidm", "etc/kanidm/config"]


@subpackage("kanidm-server")
def _(self):
    self.subdesc = "kanidm server daemon"
    return [
        "usr/bin/kanidmd",
        "usr/lib/dinit.d/kanidmd",
        "usr/lib/sysusers.d/kanidmd.conf",
        "usr/lib/tmpfiles.d/kanidmd.conf",
        "usr/share/kanidm",
        "etc/kanidm/server.toml",
    ]


@subpackage("kanidm-unixd-clients")
def _(self):
    self.subdesc = "kanidm unix daemon and pam / nss libraries"
    return [
        "usr/bin/kanidm_ssh_authorizedkeys",
        "usr/bin/kanidm_ssh_authorizedkeys_direct",
        "usr/bin/kanidm-unix",
        "usr/bin/kanidm_unixd",
        "usr/bin/kanidm_unixd_tasks",
        "usr/lib/libnss_kanidm.so.2",
        "usr/lib/security/pam_kanidm.so",
        "usr/lib/dinit.d/kanidm-unixd",
        "usr/lib/dinit.d/kanidm-unixd-tasks",
        "usr/lib/sysusers.d/kanidm-unixd.conf",
        "usr/lib/tmpfiles.d/kanidm-unixd.conf",
        "etc/kanidm/unixd",
    ]
