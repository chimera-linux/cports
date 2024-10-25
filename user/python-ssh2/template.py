pkgname = "python-ssh2"
pkgver = "1.0.0"
pkgrel = 0
build_style = "python_pep517"
make_build_env = {
    "SSH2_PYTHON_VERSION": pkgver,
    "SYSTEM_LIBSSH2": "1",
}
hostmakedepends = [
    "python-build",
    "python-cython",
    "python-installer",
    "python-setuptools",
]
makedepends = [
    "libssh2-devel",
    "python-devel",
]
checkdepends = [
    "openssh",
    "python-jinja2",
    "python-pytest",
]
pkgdesc = "Python bindings for libssh2"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "LGPL-2.1-only"
url = "https://github.com/ParallelSSH/ssh2-python"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "70c6b6efd8ca9f8de9c2d77e7cb1d5859542588347ea426d6822b0ffd9889af3"


# this is identical to the default check, we just have to change the pytest invocation
def check(self):
    whl = list(
        map(
            lambda p: str(p.relative_to(self.cwd)),
            self.cwd.glob("dist/*.whl"),
        )
    )

    self.rm(".cbuild-checkenv", recursive=True, force=True)
    self.do(
        "python3",
        "-m",
        "venv",
        "--without-pip",
        "--system-site-packages",
        "--clear",
        ".cbuild-checkenv",
    )

    envpy = self.chroot_cwd / ".cbuild-checkenv/bin/python3"

    self.do(envpy, "-m", "installer", *whl)
    self.do(
        envpy,
        # can't be -m pytest, otherwise it adds cwd to sys.path
        "/usr/bin/pytest",
        # use installed ssh2 module
        "--import-mode=importlib",
        "-k",
        # these require an ssh agent
        "not test_agent_get_identities"
        + " and not test_agent_id_path"
        + " and not test_agent"
        + " and not test_failed_agent_auth"
        # ssh2.exceptions.SocketRecvError
        + " and not test_sftp_symlink_realpath_lstat"
        + " and not test_sftp_write"
        + " and not test_statvfs"
        + " and not SessionTestCase"
        # ssh2.exceptions.AuthenticationError
        + " and not test_direct_tcpip"
        + " and not ChannelTestCase"
        + " and not KnownHostTestCase"
        + " and not SFTPTestCase"
        # ssh2.exceptions.SocketDisconnectError
        + " and not test_non_blocking"
        + " and not test_pubkey_auth"
        + " and not test_scp_recv"
        + " and not test_publickey_frommemory",
        path=[envpy.parent],
    )
